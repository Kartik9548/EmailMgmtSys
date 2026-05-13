from googleapiclient.discovery import build
from app.modules.auth import refresh_credentials
from datetime import datetime, timedelta
import pytz

def get_calendar_service(user_creds):
    """Create Calendar service with user credentials"""
    creds_data = user_creds.get('credentials')
    credentials = refresh_credentials(creds_data)
    return build('calendar', 'v3', credentials=credentials)

def get_calendar_events(user, days_ahead=30):
    """
    Fetch calendar events
    
    Args:
        user: User session data
        days_ahead: Number of days to look ahead
    
    Returns:
        List of events
    """
    try:
        service = get_calendar_service(user)
        
        now = datetime.utcnow().isoformat() + 'Z'
        end_date = (datetime.utcnow() + timedelta(days=days_ahead)).isoformat() + 'Z'
        
        # Get events from primary calendar
        events_result = service.events().list(
            calendarId='primary',
            timeMin=now,
            timeMax=end_date,
            singleEvents=True,
            orderBy='startTime',
            maxResults=25
        ).execute()
        
        events = events_result.get('items', [])
        
        # Format events for display
        formatted_events = []
        for event in events:
            formatted_events.append({
                'id': event['id'],
                'summary': event.get('summary', 'No Title'),
                'start': event['start'].get('dateTime', event['start'].get('date')),
                'end': event['end'].get('dateTime', event['end'].get('date')),
                'description': event.get('description', ''),
                'location': event.get('location', ''),
                'attendees': [a['email'] for a in event.get('attendees', [])],
                'organizer': event.get('organizer', {}).get('email', ''),
                'htmlLink': event.get('htmlLink', '')
            })
        
        return formatted_events
    
    except Exception as e:
        print(f"Error fetching calendar events: {e}")
        return []

def create_event(user, event_data):
    """Create a new calendar event"""
    try:
        service = get_calendar_service(user)
        
        event = {
            'summary': event_data.get('title'),
            'description': event_data.get('description'),
            'start': {
                'dateTime': event_data.get('start_time'),
                'timeZone': 'UTC'
            },
            'end': {
                'dateTime': event_data.get('end_time'),
                'timeZone': 'UTC'
            }
        }
        
        created_event = service.events().insert(calendarId='primary', body=event).execute()
        
        return {'success': True, 'event_id': created_event['id']}
    
    except Exception as e:
        print(f"Error creating event: {e}")
        return {'success': False, 'error': str(e)}

def delete_event(user, event_id):
    """Delete a calendar event"""
    try:
        service = get_calendar_service(user)
        service.events().delete(calendarId='primary', eventId=event_id).execute()
        return {'success': True}
    
    except Exception as e:
        print(f"Error deleting event: {e}")
        return {'success': False, 'error': str(e)}
