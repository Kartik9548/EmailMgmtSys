from flask import Blueprint, render_template, redirect, url_for, session, request, jsonify
from app.modules.auth import authenticate_google, get_user_info, logout_user
from app.modules.email_handler import get_emails, send_email, get_attachments
from app.modules.calendar_handler import get_calendar_events
import functools

# Blueprints
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
email_bp = Blueprint('email', __name__, url_prefix='/email')
calendar_bp = Blueprint('calendar', __name__, url_prefix='/calendar')

# Middleware to check authentication
def login_required(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

# ==================== AUTH ROUTES ====================
@auth_bp.route('/login')
def login():
    auth_url = authenticate_google()
    return redirect(auth_url)

@auth_bp.route('/callback')
def callback():
    user_info = get_user_info(request.args.get('code'))
    if user_info:
        session['user'] = user_info
        return redirect(url_for('email.dashboard'))
    return redirect(url_for('auth.login'))

@auth_bp.route('/logout')
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('email.index'))

# ==================== EMAIL ROUTES ====================
@email_bp.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('email.dashboard'))
    return render_template('index.html')

@email_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=session.get('user'))

@email_bp.route('/inbox')
@login_required
def inbox():
    emails = get_emails(session.get('user'), folder='INBOX')
    return render_template('inbox.html', emails=emails, user=session.get('user'))

@email_bp.route('/sent')
@login_required
def sent():
    emails = get_emails(session.get('user'), folder='SENT')
    return render_template('emails.html', emails=emails, folder='SENT', user=session.get('user'))

@email_bp.route('/drafts')
@login_required
def drafts():
    emails = get_emails(session.get('user'), folder='DRAFTS')
    return render_template('emails.html', emails=emails, folder='DRAFTS', user=session.get('user'))

@email_bp.route('/compose', methods=['GET', 'POST'])
@login_required
def compose():
    if request.method == 'POST':
        result = send_email(session.get('user'), request.form)
        return jsonify(result)
    return render_template('compose.html', user=session.get('user'))

@email_bp.route('/search')
@login_required
def search():
    query = request.args.get('q', '')
    emails = get_emails(session.get('user'), search_query=query)
    return render_template('emails.html', emails=emails, search_query=query, user=session.get('user'))

@email_bp.route('/email/<email_id>')
@login_required
def view_email(email_id):
    email_data = get_emails(session.get('user'), email_id=email_id)
    return render_template('email_view.html', email=email_data, user=session.get('user'))

# ==================== CALENDAR ROUTES ====================
@calendar_bp.route('/events')
@login_required
def events():
    events = get_calendar_events(session.get('user'))
    return render_template('calendar.html', events=events, user=session.get('user'))

@calendar_bp.route('/api/events')
@login_required
def api_events():
    events = get_calendar_events(session.get('user'))
    return jsonify(events)
