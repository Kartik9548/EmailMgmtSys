# Contributing & Architecture Guide

## System Architecture

### Tech Stack
- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Authentication**: Google OAuth2
- **APIs**: Gmail API v1, Google Calendar v3
- **Session Management**: Flask-Session (filesystem)
- **No Database**: Uses OAuth credentials for state management

### Data Flow

```
1. User Login Flow:
   User → Login Button → Google OAuth → Get Access Token → Store in Session

2. Email Fetch Flow:
   User clicks Inbox → Route /email/inbox → get_emails() → Gmail API → Display

3. Send Email Flow:
   User fills form → POST /email/compose → send_email() → Gmail API → Sent folder

4. Calendar Fetch Flow:
   User clicks Calendar → Route /calendar/events → get_calendar_events() → Calendar API
```

---

## Code Structure & Best Practices

### Module Organization

#### `app/__init__.py` - App Factory
```python
# Creates Flask app with blueprints
def create_app():
    app = Flask(__name__)
    # Config
    # Init Session
    # Register blueprints
    return app
```

#### `app/routes.py` - URL Routing
```python
# Blueprint structure:
# - auth_bp: /auth/* (login, callback, logout)
# - email_bp: /email/* (inbox, sent, compose, search)
# - calendar_bp: /calendar/* (events, create, delete)
```

#### `app/modules/` - Business Logic
- **auth.py**: OAuth2 credential management
- **email_handler.py**: Gmail API operations
- **calendar_handler.py**: Calendar API operations

### Key Design Patterns

1. **Session-Based State**: No database needed
   ```python
   session['user'] = {
       'email': 'user@gmail.com',
       'credentials': {...}  # OAuth tokens
   }
   ```

2. **Decorator-Based Auth**: Protect routes
   ```python
   @login_required
   def protected_route():
       pass
   ```

3. **Blueprint Organization**: Modular routes
   ```python
   email_bp = Blueprint('email', __name__)
   # Register in app factory
   ```

4. **API Wrapper Functions**: Abstract complexity
   ```python
   get_gmail_service(user)  # Creates service once
   ```

---

## Adding New Features

### Example: Add "Mark as Spam" Feature

**Step 1: Add to email_handler.py**
```python
def mark_as_spam(user, email_id):
    """Mark email as spam"""
    try:
        service = get_gmail_service(user)
        service.users().messages().modify(
            userId='me',
            id=email_id,
            body={'addLabelIds': ['SPAM']}
        ).execute()
        return {'success': True}
    except Exception as e:
        return {'success': False, 'error': str(e)}
```

**Step 2: Add route to routes.py**
```python
@email_bp.route('/email/<email_id>/spam', methods=['POST'])
@login_required
def mark_spam(email_id):
    result = mark_as_spam(session.get('user'), email_id)
    return jsonify(result)
```

**Step 3: Add button to template**
```html
<button onclick="markSpam('{{ email.id }}')">Mark as Spam</button>
```

**Step 4: Add JavaScript**
```javascript
async function markSpam(emailId) {
    const response = await fetch(`/email/${emailId}/spam`, {
        method: 'POST'
    });
    const data = await response.json();
    if (data.success) {
        showNotification('Marked as spam');
    }
}
```

---

## Testing Checklist

### Authentication Tests
- [ ] Login with Google works
- [ ] Session persists across pages
- [ ] Logout clears session
- [ ] Unauthorized access redirects to login

### Email Tests
- [ ] Can view inbox emails
- [ ] Can send email successfully
- [ ] Can view sent emails
- [ ] Can search emails
- [ ] Can download attachments
- [ ] Filters work (unread, starred)

### Calendar Tests
- [ ] Can view upcoming events
- [ ] Event details display correctly
- [ ] Multiple events show properly

### UI/UX Tests
- [ ] All buttons are clickable
- [ ] Forms validate input
- [ ] Responsive on mobile
- [ ] No JavaScript errors in console

---

## Performance Optimization

### Current Approach
- Max 10 emails per page (configurable)
- Events fetched for 30 days ahead
- Session-based caching

### Optimization Ideas
1. **Pagination**: Load more emails on scroll
2. **Client-side Caching**: Cache emails temporarily
3. **API Response Caching**: Cache for 5 minutes
4. **Lazy Loading**: Load images/attachments on demand
5. **Background Tasks**: Celery for email sync

---

## Security Considerations

### Current Security
✅ OAuth2 (no passwords stored)
✅ Session tokens (Flask-Session)
✅ Secure cookie handling
✅ HTTPS ready

### Security Improvements
- [ ] CSRF token validation
- [ ] Rate limiting on API calls
- [ ] Input sanitization (HTML escaping)
- [ ] API key rotation
- [ ] Audit logging
- [ ] End-to-end encryption option

---

## Debugging Guide

### Enable Debug Mode
```python
# In run.py
app.run(debug=True)
```

### View Logs
```bash
# Terminal shows all Flask logs
# Check for errors after actions
```

### Check Session Data
```python
# In routes
print(session)  # See what's stored
```

### Test API Directly
```python
# In Python shell
from app.modules.email_handler import get_emails
emails = get_emails(user_data)
```

---

## File Modification Checklist

### When Adding Routes
- [ ] Add to appropriate blueprint
- [ ] Add @login_required if needed
- [ ] Handle errors with try/except
- [ ] Return JSON for API endpoints
- [ ] Return rendered template for pages

### When Adding Templates
- [ ] Extend base.html
- [ ] Use consistent styling classes
- [ ] Add form validation (client + server)
- [ ] Test on mobile (responsive)
- [ ] Use semantic HTML

### When Adding Modules
- [ ] Import at top of file
- [ ] Add docstrings to functions
- [ ] Handle exceptions gracefully
- [ ] Return consistent data formats
- [ ] Add to requirements.txt if new package

---

## Common Errors & Fixes

| Error | Cause | Solution |
|-------|-------|----------|
| `403 Insufficient Permissions` | OAuth scope missing | Add scope to SCOPES list |
| `401 Unauthorized` | Invalid/expired token | Token refresh in auth.py |
| `Message not found` | Wrong email ID | Check email exists |
| `Rate limit exceeded` | Too many API calls | Implement caching |

---

## Git Workflow

```bash
# Start feature
git checkout -b feature/email-templates

# Make changes
# Test thoroughly

# Commit
git commit -m "feat: add email templates"

# Push
git push origin feature/email-templates

# Create PR
# Review & merge
```

### Commit Message Format
```
feat: add email templates
fix: resolve inbox loading issue
docs: update README
refactor: simplify email parsing
test: add OAuth tests
```

---

## Deployment Checklist

Before deploying to production:

- [ ] Set DEBUG=False
- [ ] Use secure SECRET_KEY
- [ ] Enable HTTPS only
- [ ] Add rate limiting
- [ ] Setup error logging
- [ ] Test with real Gmail account
- [ ] Add CORS headers if needed
- [ ] Setup backup/restore
- [ ] Monitor API usage
- [ ] Create privacy policy

---

## Future Roadmap

### Phase 1 (Current)
- ✅ Basic email management
- ✅ Calendar integration
- ✅ Web UI

### Phase 2 (Next)
- [ ] Outlook integration
- [ ] Multiple account support
- [ ] Email labels/tags
- [ ] Advanced filters

### Phase 3 (Long-term)
- [ ] Mobile app (React Native)
- [ ] Desktop app (Electron)
- [ ] Email encryption
- [ ] Scheduled sending
- [ ] Analytics dashboard

---

## Resources for Developers

### Google APIs Documentation
- [Gmail API](https://developers.google.com/gmail/api/reference/rest)
- [Calendar API](https://developers.google.com/calendar/api/guides/overview)
- [OAuth2 Guide](https://developers.google.com/identity/protocols/oauth2)

### Flask Resources
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Jinja2 Templates](https://jinja.palletsprojects.com/)
- [Flask Blueprints](https://flask.palletsprojects.com/blueprints/)

### Best Practices
- [REST API Design](https://restfulapi.net/)
- [Clean Code](https://clean-code-python.readthedocs.io/)
- [Security Headers](https://owasp.org/www-project-secure-headers/)

---

## Questions?

Refer to:
1. README.md - General overview
2. GETTING_STARTED.md - Setup & usage
3. Inline code comments - Implementation details
4. Google API docs - API-specific questions

Happy coding! 🎉
