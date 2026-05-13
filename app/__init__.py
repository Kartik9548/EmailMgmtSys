from flask import Flask, redirect, url_for
from flask_session import Session
import os

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['PERMANENT_SESSION_LIFETIME'] = 3600
    
    # Initialize Session
    Session(app)
    
    # Register Blueprints
    from app.routes import auth_bp, email_bp, calendar_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(email_bp)
    app.register_blueprint(calendar_bp)
    
    # Root route
    @app.route('/')
    def root():
        return redirect(url_for('email.index'))
    
    return app
