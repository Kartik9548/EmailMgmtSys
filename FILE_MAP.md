# Email Management System - File Directory Map

## Complete Project Structure

```
EmailManagementSystem/
│
├── 📍 Root Configuration Files
│   ├── run.py                          ⭐ START HERE - python run.py
│   ├── requirements.txt                All Python dependencies
│   ├── .env.example                    Environment variables template
│   └── .gitignore                      Git ignore rules
│
├── 📚 Documentation (Read These!)
│   ├── README.md                       ⭐ COMPREHENSIVE GUIDE
│   ├── GETTING_STARTED.md              ⭐ 5-STEP SETUP GUIDE
│   ├── ARCHITECTURE.md                 ⭐ DEVELOPER GUIDE
│   ├── PROJECT_SUMMARY.md              Project overview & features
│   └── QUICK_REFERENCE.md              Quick lookup guide
│
└── 📦 app/ (Main Application)
    │
    ├── __init__.py
    │   └── Contains: Flask app factory, blueprint registration
    │       Key Functions: create_app()
    │
    ├── routes.py (THE MAIN ROUTER)
    │   └── Contains: All URL endpoints
    │       Key Sections:
    │       • Auth routes (lines 21-42)
    │           /auth/login, /auth/callback, /auth/logout
    │       • Email routes (lines 46-75)
    │           /email/*, /email/dashboard, /email/inbox, etc.
    │       • Calendar routes (lines 79-87)
    │           /calendar/events, /calendar/api/events
    │
    ├── 📁 modules/ (Business Logic Layer)
    │   │
    │   ├── __init__.py
    │   │
    │   ├── auth.py (AUTHENTICATION)
    │   │   Functions:
    │   │   • authenticate_google()        Generate OAuth URL
    │   │   • get_user_info()              Exchange code for credentials
    │   │   • logout_user()                Clear user session
    │   │   • refresh_credentials()        Refresh expired tokens
    │   │
    │   ├── email_handler.py (EMAIL OPERATIONS)
    │   │   Functions:
    │   │   • get_gmail_service()          Create service instance
    │   │   • get_emails()                 Fetch emails from folders
    │   │   • send_email()                 Send new email
    │   │   • parse_email()                Convert API response to object
    │   │   • get_email_body()             Extract body from email
    │   │   • filter_emails()              Filter by unread/starred
    │   │   • get_attachments()            Download file attachments
    │   │
    │   └── calendar_handler.py (CALENDAR OPERATIONS)
    │       Functions:
    │       • get_calendar_service()       Create service instance
    │       • get_calendar_events()        Fetch upcoming events
    │       • create_event()               Create new calendar event
    │       • delete_event()               Remove event
    │
    ├── 📁 templates/ (HTML Pages - Jinja2)
    │   │
    │   ├── base.html
    │   │   └── Navigation bar, layout structure
    │   │       Contains: Navbar, footer, alert system
    │   │       Extends: None (base template)
    │   │       Extends to: All other templates
    │   │
    │   ├── index.html (LOGIN PAGE)
    │   │   └── Beautiful login page with feature list
    │   │       Shows: When user is not logged in
    │   │       Contains: OAuth button, feature highlights
    │   │
    │   ├── dashboard.html (MAIN HUB)
    │   │   └── Dashboard with quick links
    │   │       Shows: After login
    │   │       Features: 6 main cards (Inbox, Compose, Sent, etc.)
    │   │
    │   ├── inbox.html (EMAIL LIST)
    │   │   └── Display list of emails
    │   │       Shows: Email list with filters
    │   │       Features: Checkboxes, filter buttons, email preview
    │   │
    │   ├── compose.html (EMAIL COMPOSER)
    │   │   └── Compose and send emails
    │   │       Contains: To, Subject, Body fields
    │   │       Features: Email templates, attachment upload
    │   │       Templates: Greeting, Follow-up, Support Request
    │   │
    │   ├── calendar.html (CALENDAR VIEW)
    │   │   └── Display calendar events
    │   │       Shows: Next 30 days of events
    │   │       Features: Event cards with details
    │   │
    │   ├── email_view.html (FULL EMAIL VIEW)
    │   │   └── Display single email in full
    │   │       Shows: All email details and attachments
    │   │       Features: Reply, Forward, Delete buttons
    │   │
    │   └── emails.html (GENERIC EMAIL LIST)
    │       └── Reusable email list template
    │           Shows: Sent, Drafts, or search results
    │           Features: Same as inbox
    │
    ├── 📁 static/ (Frontend Assets)
    │   │
    │   ├── 📁 css/
    │   │   └── style.css (COMPLETE STYLING - 500+ lines)
    │   │       Sections:
    │   │       • Root variables (colors, fonts)
    │   │       • Body & layout
    │   │       • Navbar styling
    │   │       • Buttons (.btn, .btn-primary, etc.)
    │   │       • Login page (.login-page, .login-box)
    │   │       • Forms (.form-group)
    │   │       • Alerts (.alert, .alert-success)
    │   │       • Email lists (.email-item, .email-list)
    │   │       • Dashboard cards (.dashboard-card)
    │   │       • Footer
    │   │       • Responsive media queries
    │   │       • Utilities (text-center, margins, etc.)
    │   │
    │   └── 📁 js/
    │       └── main.js (JAVASCRIPT INTERACTIONS - 200+ lines)
    │           Functions:
    │           • initializeApp()          Initialize on page load
    │           • setupFilterButtons()     Setup email filters
    │           • setupSearchForm()        Setup search
    │           • filterEmails()           Filter emails client-side
    │           • selectAllEmails()        Select all checkboxes
    │           • deleteSelectedEmails()   Bulk delete
    │           • markAsRead/Unread()      Mark email status
    │           • starEmail/unstarEmail()  Star emails
    │           • showNotification()       Toast notifications
    │           • apiCall()                Generic API caller
    │
    └── 📄 .env (NOT TRACKED - CREATE THIS)
        └── Contains:
            GOOGLE_CLIENT_ID=your_id
            GOOGLE_CLIENT_SECRET=your_secret
            SECRET_KEY=your_key
            Etc.
```

---

## 🎯 File Purposes Quick Map

### Must Edit Files
1. `.env` - Add your Google OAuth credentials
2. `run.py` - Change port if needed

### Don't Edit Initially
- `requirements.txt` - Dependencies list
- All app files - They're ready to use!

### Read These
1. `README.md` - Complete documentation
2. `GETTING_STARTED.md` - Setup instructions
3. `ARCHITECTURE.md` - How it works
4. `QUICK_REFERENCE.md` - Cheatsheet

### Extend With
- `app/modules/` - Add new business logic
- `app/routes.py` - Add new URL routes
- `app/templates/` - Add new pages
- `app/static/css/` - Add new styles
- `app/static/js/` - Add new interactions

---

## 📊 File Statistics

```
Backend (Python)
├── routes.py                 ~150 lines
├── auth.py                   ~80 lines
├── email_handler.py          ~200 lines
├── calendar_handler.py       ~120 lines
└── __init__.py               ~20 lines
   Total: ~570 lines

Frontend (HTML/CSS/JS)
├── HTML Templates            ~800 lines (8 files)
├── CSS (style.css)           ~700 lines
├── JS (main.js)              ~200 lines
└── Configuration             ~50 lines
   Total: ~1,750 lines

Documentation
├── README.md                 ~300 lines
├── GETTING_STARTED.md        ~400 lines
├── ARCHITECTURE.md           ~350 lines
├── PROJECT_SUMMARY.md        ~400 lines
├── QUICK_REFERENCE.md        ~300 lines
└── ARCHITECTURE.md           ~350 lines
   Total: ~2,100 lines

Grand Total: ~4,400+ lines of code & documentation
```

---

## 🔄 Data Flow Maps

### Authentication Flow
```
User Browser
    ↓ (Click Login)
run.py → Flask
    ↓
routes.py → auth_bp.login()
    ↓
auth.py → authenticate_google()
    ↓ (Redirect)
Google OAuth Server
    ↓ (User authorizes)
Redirect back to /auth/callback
    ↓
routes.py → auth_bp.callback()
    ↓
auth.py → get_user_info()
    ↓
session['user'] = {...}
    ↓ (Redirect)
routes.py → email_bp.dashboard()
    ↓
Dashboard displays
```

### Email Fetch Flow
```
User clicks Inbox
    ↓
routes.py → email_bp.inbox()
    ↓
email_handler.py → get_emails(user, folder='INBOX')
    ↓
Gmail API (via google-api-client)
    ↓ (Returns message list)
email_handler.py → parse_email()
    ↓ (Converts to dict)
routes.py → render_template('inbox.html', emails=[...])
    ↓
Jinja2 renders HTML
    ↓
style.css applies styling
    ↓
main.js adds interactivity
    ↓
User sees inbox
```

### Email Send Flow
```
User fills compose form
    ↓
compose.html (form submit)
    ↓
JavaScript posts data
    ↓
routes.py → email_bp.compose()
    ↓
email_handler.py → send_email()
    ↓ (Creates MIME message)
Gmail API (sends)
    ↓ (Returns response)
JSON response sent back
    ↓
main.js shows success notification
    ↓
Redirect to sent folder
```

---

## 🎯 Common File Edits

### Add New Email Feature
1. **Logic** → `app/modules/email_handler.py`
2. **Route** → `app/routes.py` (under `email_bp`)
3. **Template** → `app/templates/new_template.html`
4. **Styling** → `app/static/css/style.css`
5. **Interaction** → `app/static/js/main.js`

### Add New Page
1. Create `app/templates/newpage.html`
2. Add route in `app/routes.py`
3. Add styling in `style.css`
4. Add link to `base.html` navbar

### Add Authentication to Route
```python
@email_bp.route('/protected')
@login_required
def protected_route():
    user = session.get('user')
    # Your code
```

---

## 🔗 File Relationships

```
run.py (Entry Point)
    ↓
app/__init__.py (Flask app setup)
    ↓
app/routes.py (URL routing)
    ├─ Uses: app/modules/auth.py
    ├─ Uses: app/modules/email_handler.py
    ├─ Uses: app/modules/calendar_handler.py
    ├─ Renders: app/templates/*.html
    ├─ Uses: app/static/css/style.css
    └─ Uses: app/static/js/main.js

Templates use:
    ├─ base.html (parent)
    ├─ style.css (styling)
    └─ main.js (interactions)
```

---

## 📝 Documentation Map

```
Need help with...        Read this file
├─ Getting started       → GETTING_STARTED.md
├─ Complete overview     → README.md
├─ Architecture details  → ARCHITECTURE.md
├─ Quick lookup         → QUICK_REFERENCE.md
├─ Project summary      → PROJECT_SUMMARY.md
├─ Code structure       → This file (FILE_MAP.md)
└─ Specific feature     → Inline code comments
```

---

## ✅ File Checklist

After setup, you should have:

- ✅ `run.py` - Entry point
- ✅ `requirements.txt` - Dependencies  
- ✅ `.env.example` - Config template
- ✅ `.gitignore` - Git rules
- ✅ 5 documentation files
- ✅ `app/__init__.py` - App factory
- ✅ `app/routes.py` - Routes
- ✅ 3 module files (auth, email, calendar)
- ✅ 8 HTML templates
- ✅ `style.css` - Styling
- ✅ `main.js` - JavaScript
- ✅ `credentials.json` ← YOU CREATE THIS

---

## 🚀 Next: Run the App

```bash
# From EmailManagementSystem directory
python run.py

# Then visit
http://localhost:5000
```

**You're all set!** 🎉

---

*This file maps the complete project structure and relationships.*
*Last updated: May 13, 2026*
