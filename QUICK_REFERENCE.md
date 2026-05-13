# 📋 Email Management System - Quick Reference

## 🚀 Start in 5 Steps

```bash
# 1. Navigate to project
cd EmailManagementSystem

# 2. Create & activate virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add Google OAuth credentials
# Download from Google Cloud Console → Save as credentials.json

# 5. Run the app
python run.py
# Visit: http://localhost:5000
```

---

## 📁 File Locations

| What | Where |
|------|-------|
| Start App | `run.py` |
| Email Routes | `app/routes.py` (lines 30-60) |
| Email Logic | `app/modules/email_handler.py` |
| Templates | `app/templates/*.html` |
| Styling | `app/static/css/style.css` |
| JavaScript | `app/static/js/main.js` |

---

## 🎯 Main Features

### 1. Authentication
**File**: `app/modules/auth.py`
```python
authenticate_google()       # Get OAuth URL
get_user_info(code)        # Exchange code for credentials
refresh_credentials()      # Refresh expired tokens
```

### 2. Email Management
**File**: `app/modules/email_handler.py`
```python
get_emails()               # Fetch inbox/sent/drafts
send_email()               # Send new email
filter_emails()            # Filter by type
get_attachments()          # Download files
```

### 3. Calendar
**File**: `app/modules/calendar_handler.py`
```python
get_calendar_events()      # Fetch upcoming events
create_event()             # Create new event
delete_event()             # Remove event
```

---

## 🔗 URL Routes

| URL | Purpose | Method |
|-----|---------|--------|
| `/` | Home/Login | GET |
| `/auth/login` | Start OAuth | GET |
| `/auth/callback` | OAuth return | GET |
| `/email/dashboard` | Main hub | GET |
| `/email/inbox` | View inbox | GET |
| `/email/sent` | View sent | GET |
| `/email/compose` | Composer | GET/POST |
| `/email/search?q=term` | Search | GET |
| `/email/<id>` | View email | GET |
| `/calendar/events` | Calendar | GET |

---

## 🎨 Templates

| Template | Purpose | Location |
|----------|---------|----------|
| base.html | Navigation & layout | app/templates/base.html |
| index.html | Login page | app/templates/index.html |
| dashboard.html | Main dashboard | app/templates/dashboard.html |
| inbox.html | Email list | app/templates/inbox.html |
| compose.html | Email composer | app/templates/compose.html |
| calendar.html | Calendar view | app/templates/calendar.html |

---

## 💾 Data Format

### Session Data
```python
session['user'] = {
    'email': 'user@gmail.com',
    'credentials': {
        'token': '...',
        'refresh_token': '...',
        'token_uri': '...',
        'client_id': '...',
        'client_secret': '...',
        'scopes': [...]
    }
}
```

### Email Object
```python
{
    'id': 'email_id',
    'threadId': 'thread_id',
    'from': 'sender@gmail.com',
    'to': 'recipient@gmail.com',
    'subject': 'Email Subject',
    'date': '2026-05-13',
    'body': 'Email content...',
    'snippet': 'Preview...',
    'labels': ['UNREAD', 'IMPORTANT'],
    'attachments': [
        {
            'filename': 'file.pdf',
            'mimeType': 'application/pdf',
            'attachmentId': '...'
        }
    ]
}
```

### Calendar Event
```python
{
    'id': 'event_id',
    'summary': 'Event Title',
    'start': '2026-05-13T10:00:00Z',
    'end': '2026-05-13T11:00:00Z',
    'description': 'Event details...',
    'location': 'Meeting Room',
    'attendees': ['user@gmail.com'],
    'organizer': 'organizer@gmail.com',
    'htmlLink': 'https://calendar.google.com/...'
}
```

---

## 🛠️ Common Tasks

### Add New Route
```python
# In app/routes.py
@email_bp.route('/email/new_feature')
@login_required
def new_feature():
    # Your code here
    return render_template('template.html')
```

### Add New Template
```bash
# Create app/templates/new_template.html
{% extends "base.html" %}
{% block content %}
    <h1>Your content</h1>
{% endblock %}
```

### Call API from JavaScript
```javascript
// In app/static/js/main.js
async function apiCall(endpoint, method = 'GET', data = null) {
    const response = await fetch(endpoint, {
        method: method,
        headers: {'Content-Type': 'application/json'},
        body: data ? JSON.stringify(data) : null
    });
    return await response.json();
}
```

### Debug Session Data
```python
# In routes.py
print(session.get('user'))  # Print user data
print(session.keys())       # Print all keys
```

---

## 🔑 Environment Variables

```env
GOOGLE_CLIENT_ID=your_id_here
GOOGLE_CLIENT_SECRET=your_secret_here
SECRET_KEY=your_secret_key
FLASK_ENV=development
FLASK_DEBUG=True
SESSION_TYPE=filesystem
```

---

## 📦 Key Dependencies

```
Flask==3.0.0                          # Web framework
google-auth-oauthlib==1.1.0          # OAuth2
google-api-python-client==2.108.0    # Gmail & Calendar API
python-dotenv==1.0.0                 # Env variables
```

---

## 🧪 Testing Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run app
python run.py

# Test email fetch
# Visit: http://localhost:5000 → Login → Inbox

# Check logs
# Look in terminal where you ran python run.py

# Debug Python
python -c "from app import create_app; print(create_app())"
```

---

## 🐛 Quick Fixes

| Problem | Solution |
|---------|----------|
| Port in use | Edit `run.py`: `app.run(port=5001)` |
| No credentials | Download from Google Cloud Console |
| OAuth error | Update redirect URI in Google Console |
| Emails not loading | Enable Gmail API in Google Cloud |
| Module import error | Run: `pip install -r requirements.txt` |

---

## 📚 Documentation

| Document | For |
|----------|-----|
| `README.md` | Complete documentation |
| `GETTING_STARTED.md` | Setup & usage guide |
| `ARCHITECTURE.md` | Development guide |
| `PROJECT_SUMMARY.md` | Project overview |
| This file | Quick reference |

---

## 🎓 Key Concepts

### Flask Blueprint
Modular route organization
```python
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
```

### Session Decorator
Protect routes requiring login
```python
@login_required
def protected_route():
    pass
```

### Jinja2 Template
HTML with Python variables
```html
<p>{{ user.email }}</p>
```

### OAuth2 Flow
1. User clicks login
2. Redirected to Google
3. Google redirects back with code
4. App exchanges code for credentials
5. Credentials stored in session

---

## 💡 Pro Tips

1. **Enable Debug Mode** for better error messages
2. **Use Chrome DevTools** to inspect frontend
3. **Check Flask logs** in terminal for backend errors
4. **Test API manually** using Google API Explorer
5. **Cache credentials** to reduce API calls
6. **Add rate limiting** before deploying

---

## 🔄 Common Workflows

### Login Flow
User → Login Page → Click "Login with Google" → OAuth → Redirected to Dashboard

### Send Email Workflow
Dashboard → Compose → Fill Form → Select Template → Send → Redirected to Sent

### View Email Workflow
Inbox → Click Email → Full View → See Body, Attachments, Actions

### Search Workflow
Any Page → Enter Query → Submit → Results Displayed

---

## 📊 Architecture Overview

```
┌─────────────────────────────────┐
│      User's Browser             │
└───────────────┬─────────────────┘
                │ HTTP
                ▼
┌─────────────────────────────────┐
│      Flask Web Server           │
│  ├─ Routes (routes.py)          │
│  ├─ Auth Module (auth.py)       │
│  ├─ Email Module (email_handler)│
│  ├─ Calendar Module (calendar)  │
└───────────────┬─────────────────┘
                │ API Calls
        ┌───────┴────────┐
        ▼                ▼
    Gmail API      Calendar API
        ▼                ▼
   User's Gmail   User's Calendar
```

---

## ✅ Deployment Checklist

- [ ] Set `DEBUG=False` in `run.py`
- [ ] Use strong `SECRET_KEY`
- [ ] Enable HTTPS only
- [ ] Test with real Gmail account
- [ ] Add rate limiting
- [ ] Setup error logging
- [ ] Create `.env` with production values
- [ ] Test all features before deployment

---

## 🆘 Getting Help

**Error in terminal?**
→ Read the error message carefully

**Import not found?**
→ Run: `pip install -r requirements.txt`

**OAuth not working?**
→ Check `credentials.json` exists and is valid

**Emails not loading?**
→ Verify Gmail API is enabled in Google Cloud

**Still stuck?**
→ Check `GETTING_STARTED.md` or `ARCHITECTURE.md`

---

## 📞 Quick Contact

Need help? Check:
1. Error message in terminal
2. README.md (comprehensive guide)
3. GETTING_STARTED.md (setup help)
4. ARCHITECTURE.md (development questions)
5. Inline code comments

---

*Last Updated: May 13, 2026*
*Project Version: 1.0 - MVP Complete*
