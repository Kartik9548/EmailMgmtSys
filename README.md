# Email Management System

A web-based email management application built with Python Flask that integrates with Gmail and Outlook through OAuth2, allowing users to manage their emails and calendar events.

## Features

- ✅ **Send/Receive Emails**: Full email management from your Gmail account
- ✅ **User Authentication**: Secure OAuth2 authentication with Google
- ✅ **Email Organization**: Inbox, Sent, Drafts folders with filtering
- ✅ **Search Functionality**: Search emails by subject, sender, content
- ✅ **Attachments Support**: View and download email attachments
- ✅ **Email Templates**: Pre-built templates for common email types
- ✅ **Calendar Integration**: View and manage Google Calendar events
- ✅ **Interactive Web UI**: Modern, responsive user interface

## Project Structure

```
EmailManagementSystem/
├── app/
│   ├── modules/
│   │   ├── auth.py              # OAuth2 authentication
│   │   ├── email_handler.py     # Email operations
│   │   └── calendar_handler.py  # Calendar operations
│   ├── templates/
│   │   ├── base.html            # Base template
│   │   ├── index.html           # Login page
│   │   ├── dashboard.html       # Main dashboard
│   │   ├── inbox.html           # Inbox view
│   │   ├── compose.html         # Email composer
│   │   ├── calendar.html        # Calendar view
│   │   └── emails.html          # Email list view
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css        # Global styles
│   │   └── js/
│   │       └── main.js          # JavaScript
│   ├── __init__.py              # Flask app initialization
│   └── routes.py                # Route definitions
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment template
├── run.py                       # Application entry point
└── README.md                    # This file
```

## Prerequisites

- Python 3.8 or higher
- Google Cloud Console account with Gmail API enabled
- Virtual environment (recommended)

## Installation

### 1. Clone/Setup the project

```bash
cd /Users/B0334052/Desktop/DevOps/DevOpsKK/POCProject/EmailManagementSystem
```

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate  # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup Google OAuth2 Credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable Gmail API and Google Calendar API
4. Create OAuth 2.0 credentials (Web Application)
5. Add `http://localhost:5000/auth/callback` as authorized redirect URI
6. Download credentials as JSON and save as `credentials.json` in project root

### 5. Configure Environment Variables

```bash
cp .env.example .env
```

Edit `.env` and add your Google credentials:
```
GOOGLE_CLIENT_ID=your_client_id_here
GOOGLE_CLIENT_SECRET=your_client_secret_here
SECRET_KEY=your_secret_key_here
```

## Running the Application

```bash
python run.py
```

The application will start on `http://localhost:5000`

## Usage

1. **Login**: Click "Login with Google" to authenticate
2. **Dashboard**: Access main features from the dashboard
3. **Inbox**: View and manage incoming emails
4. **Compose**: Write and send new emails
5. **Calendar**: View upcoming calendar events
6. **Search**: Search for specific emails

## API Endpoints

### Authentication
- `GET /auth/login` - Initiate Google OAuth
- `GET /auth/callback` - OAuth callback
- `GET /auth/logout` - Logout

### Email Management
- `GET /email/` - Home page
- `GET /email/dashboard` - Main dashboard
- `GET /email/inbox` - View inbox
- `GET /email/sent` - View sent emails
- `GET /email/drafts` - View drafts
- `GET /email/compose` - Compose page
- `POST /email/compose` - Send email
- `GET /email/search?q=query` - Search emails
- `GET /email/<email_id>` - View specific email

### Calendar
- `GET /calendar/events` - View calendar events
- `GET /calendar/api/events` - Get events as JSON

## Future Enhancements

- [ ] Outlook integration
- [ ] Multiple account support
- [ ] Email encryption
- [ ] Advanced filtering and labels
- [ ] Email scheduling
- [ ] Spam detection
- [ ] Dark mode
- [ ] Mobile app
- [ ] Email notifications
- [ ] Backup & restore

## Dependencies

- **Flask**: Web framework
- **google-auth-oauthlib**: Google OAuth2 authentication
- **google-api-python-client**: Gmail & Calendar API
- **Flask-Session**: Server-side session management
- **python-dotenv**: Environment configuration

## Troubleshooting

### OAuth Error
- Ensure `credentials.json` is in the project root
- Check that redirect URI matches in Google Console

### Gmail API Error
- Enable Gmail API in Google Cloud Console
- Verify OAuth scopes are correct

### Port Already in Use
```bash
# Change port in run.py
app.run(port=5001)
```

## Security Notes

- Never commit `.env` or `credentials.json` to version control
- Always use HTTPS in production
- Implement rate limiting for API endpoints
- Validate all user inputs

## License

This project is provided as-is for educational purposes.

## Support

For issues and questions, please refer to the documentation or create an issue in the repository.
