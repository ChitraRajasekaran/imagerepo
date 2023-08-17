from flask import Flask, render_template,redirect,url_for,request,jsonify
from flask_sqlalchemy import SQLAlchemy

from .models import setup_db

def create_app(test_confid=None):
    app = Flask(__name__)
    with app.app_context():
        setup_db(app)

    @app.route('/')
    def display_image():
        return jsonify({'message': 'Image Repository'})
    
    return app