from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from app.modules.auth import refresh_credentials
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

def get_gmail_service(user_creds):
    """Create Gmail service with user credentials"""
    creds_data = user_creds.get('credentials')
    credentials = refresh_credentials(creds_data)
    return build('gmail', 'v1', credentials=credentials)

def get_emails(user, folder='INBOX', search_query=None, email_id=None, max_results=10):
    """
    Fetch emails from specified folder
    
    Args:
        user: User session data
        folder: Email folder (INBOX, SENT, DRAFTS)
        search_query: Optional search query
        email_id: Specific email ID to fetch
        max_results: Maximum emails to return
    
    Returns:
        List of email objects
    """
    try:
        service = get_gmail_service(user)
        
        if email_id:
            # Fetch specific email
            message = service.users().messages().get(userId='me', id=email_id, format='full').execute()
            return parse_email(message)
        
        # Build query
        query = f"in:{folder}"
        if search_query:
            query += f" {search_query}"
        
        # Get email list
        results = service.users().messages().list(
            userId='me',
            q=query,
            maxResults=max_results
        ).execute()
        
        messages = results.get('messages', [])
        emails = []
        
        for msg in messages:
            message = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
            emails.append(parse_email(message))
        
        return emails
    
    except Exception as e:
        print(f"Error fetching emails: {e}")
        return []

def parse_email(message):
    """Parse Gmail message into readable format"""
    try:
        headers = message['payload']['headers']
        
        email_data = {
            'id': message['id'],
            'threadId': message['threadId'],
            'from': next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown'),
            'to': next((h['value'] for h in headers if h['name'] == 'To'), ''),
            'subject': next((h['value'] for h in headers if h['name'] == 'Subject'), '(No Subject)'),
            'date': next((h['value'] for h in headers if h['name'] == 'Date'), ''),
            'snippet': message.get('snippet', ''),
            'labels': message.get('labelIds', []),
            'attachments': []
        }
        
        # Extract body
        body = get_email_body(message['payload'])
        email_data['body'] = body
        
        # Extract attachments
        if 'parts' in message['payload']:
            for part in message['payload']['parts']:
                if part['filename']:
                    email_data['attachments'].append({
                        'filename': part['filename'],
                        'mimeType': part['mimeType'],
                        'attachmentId': part['body'].get('attachmentId', '')
                    })
        
        return email_data
    
    except Exception as e:
        print(f"Error parsing email: {e}")
        return None

def get_email_body(payload):
    """Extract email body from payload"""
    if 'parts' in payload:
        for part in payload['parts']:
            if part['mimeType'] == 'text/plain':
                if 'data' in part['body']:
                    return base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
    else:
        if 'data' in payload['body']:
            return base64.urlsafe_b64decode(payload['body']['data']).decode('utf-8')
    
    return ''

def send_email(user, form_data):
    """Send email"""
    try:
        service = get_gmail_service(user)
        
        to = form_data.get('to')
        subject = form_data.get('subject')
        body = form_data.get('body')
        
        # Create message
        message = MIMEMultipart()
        message['to'] = to
        message['subject'] = subject
        
        message.attach(MIMEText(body, 'html'))
        
        # Handle attachments if any
        files = []  # Implement file upload handling
        
        # Send message
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        send_message = {'raw': raw_message}
        
        service.users().messages().send(userId='me', body=send_message).execute()
        
        return {'success': True, 'message': 'Email sent successfully'}
    
    except Exception as e:
        print(f"Error sending email: {e}")
        return {'success': False, 'error': str(e)}

def get_attachments(user, message_id, attachment_id):
    """Download email attachment"""
    try:
        service = get_gmail_service(user)
        
        attachment = service.users().messages().attachments().get(
            userId='me',
            messageId=message_id,
            id=attachment_id
        ).execute()
        
        file_data = base64.urlsafe_b64decode(attachment['data'].encode('UTF-8'))
        return file_data
    
    except Exception as e:
        print(f"Error downloading attachment: {e}")
        return None

def filter_emails(emails, filter_type):
    """Filter emails based on type"""
    if filter_type == 'unread':
        return [e for e in emails if 'UNREAD' in e.get('labels', [])]
    elif filter_type == 'starred':
        return [e for e in emails if 'STARRED' in e.get('labels', [])]
    elif filter_type == 'important':
        return [e for e in emails if 'IMPORTANT' in e.get('labels', [])]
    
    return emails
