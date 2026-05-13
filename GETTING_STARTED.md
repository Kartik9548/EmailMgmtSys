# Email Management System - Getting Started Guide

## Quick Start (5 Steps)

### Step 1: Setup Virtual Environment
```bash
cd /Users/B0334052/Desktop/DevOps/DevOpsKK/POCProject/EmailManagementSystem

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Setup Google OAuth2

**Important**: You need to create Google OAuth2 credentials first.

1. Go to https://console.cloud.google.com/
2. Create a new project (name it "Email Management System")
3. Enable these APIs:
   - Gmail API
   - Google Calendar API
4. Create OAuth 2.0 credentials:
   - Type: Web Application
   - Authorized redirect URIs: `http://localhost:5000/auth/callback`
5. Download credentials as JSON
6. Save as `credentials.json` in the project root

### Step 4: Configure Environment Variables
```bash
# Create .env from example
cp .env.example .env

# Edit .env and add your credentials (or just use defaults for testing)
# The app will work with any values during development
```

### Step 5: Run the Application
```bash
python run.py
```

Visit: `http://localhost:5000`

---

## Project Structure Overview

```
EmailManagementSystem/
├── app/
│   ├── __init__.py           → Flask app creation & blueprint registration
│   ├── routes.py             → All URL routes (login, inbox, compose, calendar)
│   ├── modules/              → Business logic
│   │   ├── auth.py           → Google OAuth2 authentication
│   │   ├── email_handler.py  → Email operations (send, receive, search)
│   │   └── calendar_handler.py → Calendar operations
│   ├── templates/            → HTML pages (Jinja2)
│   │   ├── base.html         → Navigation & layout
│   │   ├── index.html        → Login page
│   │   ├── dashboard.html    → Main hub
│   │   ├── inbox.html        → Email list view
│   │   ├── compose.html      → Email composer with templates
│   │   ├── calendar.html     → Calendar view
│   │   └── emails.html       → Generic email list
│   └── static/
│       ├── css/style.css     → All styling
│       └── js/main.js        → JavaScript interactions
├── run.py                    → Entry point (python run.py)
├── requirements.txt          → Python dependencies
└── README.md                 → Detailed documentation
```

---

## Key Features Explained

### 1. **Authentication** (app/modules/auth.py)
- Uses Google OAuth2 (no passwords stored)
- Securely manages user credentials
- Credentials stored in Flask sessions

### 2. **Email Operations** (app/modules/email_handler.py)
```
Functions:
- get_emails()      → Fetch from Inbox/Sent/Drafts
- send_email()      → Send new email
- filter_emails()   → Filter by unread/starred
- get_attachments() → Download attachments
```

### 3. **Calendar Integration** (app/modules/calendar_handler.py)
```
Functions:
- get_calendar_events()  → Fetch upcoming events
- create_event()         → Create new event
- delete_event()         → Delete event
```

### 4. **Routes** (app/routes.py)
| URL | Purpose |
|-----|---------|
| `/` | Home/Login page |
| `/email/dashboard` | Main dashboard |
| `/email/inbox` | View inbox |
| `/email/compose` | Write email |
| `/email/sent` | View sent emails |
| `/email/search?q=term` | Search emails |
| `/calendar/events` | View calendar |

---

## Interactive Features

### Email Composer
- **Email Templates**: Pre-built templates (Greeting, Follow-up, Support)
- **Attachments**: Upload multiple files
- **Save as Draft**: Store for later

### Email Filtering
- View all, unread, or starred emails
- Filter by folder (Inbox, Sent, Drafts)
- Full-text search across all emails

### Calendar Management
- View upcoming events
- Display event details (time, location, attendees)
- Show event descriptions

---

## Development Tips

### Adding a New Feature

1. **Create logic** in `app/modules/` if needed
2. **Add route** in `app/routes.py`
3. **Create template** in `app/templates/`
4. **Style it** in `app/static/css/style.css`

### Example: New Email Label Feature

**1. Add function in auth.py:**
```python
def create_label(user, label_name):
    service = get_gmail_service(user)
    label = {'name': label_name}
    return service.users().labels().create(userId='me', body=label).execute()
```

**2. Add route in routes.py:**
```python
@email_bp.route('/label/create', methods=['POST'])
@login_required
def create_label():
    label_name = request.form.get('name')
    result = create_label(session.get('user'), label_name)
    return jsonify(result)
```

**3. Add HTML button in template:**
```html
<button onclick="createLabel()">Create Label</button>
```

---

## Testing the App

### Test Login
1. Start app: `python run.py`
2. Visit: `http://localhost:5000`
3. Click "Login with Google"
4. Authorize the app

### Test Email Features
- **Inbox**: Should load your emails
- **Compose**: Try sending a test email
- **Search**: Search for keywords
- **Sent**: View sent emails

### Test Calendar
- Should display upcoming events
- Shows event details

---

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| `credentials.json not found` | Download from Google Cloud Console and save in project root |
| `Port 5000 in use` | Change port in `run.py`: `app.run(port=5001)` |
| `OAuth redirect URI mismatch` | Update URI in Google Cloud Console settings |
| `Emails not loading` | Check Gmail API is enabled in Google Cloud Console |
| `No calendar events` | Ensure Google Calendar API is enabled |

---

## Next Steps to Enhance

1. **Email Templates**: Add more pre-built templates
2. **Bulk Actions**: Select multiple emails and delete/move together
3. **Labels/Tags**: Create custom email labels
4. **Starred/Important**: Mark important emails
5. **Email Signatures**: Add custom signatures
6. **Dark Mode**: Add theme toggle
7. **Notifications**: Email alerts on new messages
8. **Multiple Accounts**: Support multiple Gmail accounts
9. **Advanced Search**: Filter by date, sender, size
10. **Email Encryption**: Secure email sending

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────┐
│           User's Web Browser                        │
└────────────────────┬────────────────────────────────┘
                     │ HTTP Requests
                     ▼
┌─────────────────────────────────────────────────────┐
│              Flask Web Server                       │
│  ┌──────────────────────────────────────────────┐  │
│  │ Routes (app/routes.py)                       │  │
│  │ - Login, Inbox, Compose, Calendar           │  │
│  └──────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────┐  │
│  │ Business Logic (app/modules/)                │  │
│  │ - auth.py                                    │  │
│  │ - email_handler.py                           │  │
│  │ - calendar_handler.py                        │  │
│  └──────────────────────────────────────────────┘  │
└────────────────────┬────────────────────────────────┘
                     │ API Calls
     ┌───────────────┴────────────────┐
     ▼                                 ▼
┌──────────────────┐            ┌──────────────────┐
│   Gmail API      │            │  Google Calendar │
│   (OAuth2)       │            │     API          │
└──────────────────┘            └──────────────────┘
     │                                 │
     ▼                                 ▼
┌──────────────────┐            ┌──────────────────┐
│  User's Gmail    │            │  User's Calendar │
│   Account        │            │   Account        │
└──────────────────┘            └──────────────────┘
```

---

## Learning Resources

### Flask
- https://flask.palletsprojects.com/

### Google APIs
- https://developers.google.com/gmail/api
- https://developers.google.com/calendar/api

### OAuth2
- https://oauth.net/2/
- https://tools.ietf.org/html/rfc6749

---

## Support & Help

If you encounter issues:

1. **Check README.md** for detailed troubleshooting
2. **Review logs** - Flask shows errors in terminal
3. **Test API manually** - Use Google API Explorer
4. **Check credentials** - Verify OAuth setup in Google Console

Enjoy building your email management system! 🚀
