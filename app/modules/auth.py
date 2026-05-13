import os
from google_auth_oauthlib.flow import Flow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import pickle
import json

SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/calendar.readonly'
]

def get_client_config():
    """Create client config from environment variables"""
    return {
        "installed": {
            "client_id": os.getenv('GOOGLE_CLIENT_ID'),
            "client_secret": os.getenv('GOOGLE_CLIENT_SECRET'),
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "redirect_uris": ["http://localhost:5000/auth/callback"]
        }
    }

def authenticate_google():
    """Generate Google OAuth2 authentication URL"""
    client_id = os.getenv('GOOGLE_CLIENT_ID')
    client_secret = os.getenv('GOOGLE_CLIENT_SECRET')
    
    if not client_id or not client_secret:
        raise ValueError("GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET must be set in .env file")
    
    flow = Flow.from_client_config(
        get_client_config(),
        scopes=SCOPES,
        redirect_uri='http://localhost:5000/auth/callback'
    )
    
    auth_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true'
    )
    
    return auth_url

def get_user_info(code):
    """Exchange authorization code for user credentials and info"""
    try:
        flow = Flow.from_client_config(
            get_client_config(),
            scopes=SCOPES,
            redirect_uri='http://localhost:5000/auth/callback'
        )
        
        flow.fetch_token(code=code)
        credentials = flow.credentials
        
        # Store credentials for later use
        creds_data = {
            'token': credentials.token,
            'refresh_token': credentials.refresh_token,
            'token_uri': credentials.token_uri,
            'client_id': credentials.client_id,
            'client_secret': credentials.client_secret,
            'scopes': credentials.scopes
        }
        
        # Get user email from Gmail API
        from googleapiclient.discovery import build
        gmail_service = build('gmail', 'v1', credentials=credentials)
        profile = gmail_service.users().getProfile(userId='me').execute()
        
        user_info = {
            'email': profile.get('emailAddress'),
            'credentials': creds_data
        }
        
        return user_info
    except Exception as e:
        print(f"Error authenticating: {e}")
        return None

def logout_user():
    """Logout user and revoke credentials"""
    pass

def refresh_credentials(creds_data):
    """Refresh expired credentials"""
    try:
        credentials = Credentials(
            token=creds_data.get('token'),
            refresh_token=creds_data.get('refresh_token'),
            token_uri=creds_data.get('token_uri'),
            client_id=creds_data.get('client_id'),
            client_secret=creds_data.get('client_secret'),
            scopes=creds_data.get('scopes')
        )
        
        if credentials.expired and credentials.refresh_token:
            request = Request()
            credentials.refresh(request)
        
        return credentials
    except Exception as e:
        print(f"Error refreshing credentials: {e}")
        return None
