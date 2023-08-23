from flask import Flask, render_template,redirect,url_for,request,jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
import boto3, botocore 
from botocore.config import Config
import os
from io import BytesIO
from .models import setup_db
from os import environ
from dotenv import load_dotenv

def create_app(test_confid=None):
    app = Flask(__name__)
    load_dotenv('/Users/chitrarajasekaran/Desktop/FS Practise/imagerepo/.env')

    app.config.from_pyfile('settings.py')

    session = boto3.Session(region_name='us-east-2',
                        aws_access_key_id= app.config.get("AWS_ACCESS_KEY_ID") ,
                        aws_secret_access_key = app.config.get("AWS_SECRET_ACCESS_KEY")
                    )

    s3 = session.client('s3')


    # @app.route('/')
    # def index():
    #     return f'AWS_ACCESS_KEY_ID = { app.config.get("AWS_ACCESS_KEY_ID") }'
    @app.route('/')
    def display_image():
        resource = s3.generate_presigned_url('get_object',
                                Params={'Bucket': 'qtimagerepo',
                                        'Key': 'GM 1.JPG'})
        # return jsonify({'message': resource})
        return render_template('index.html', resource=resource)



    with app.app_context():
        setup_db(app)

    return app







