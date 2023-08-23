from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer
import json
import os



database_name = "imagerepo"
database_path = "postgresql://{}@{}/{}".format('chitrarajasekaran','localhost:5432', database_name)

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

class Imagerepo(db.Model):
    __tablename__ = 'imagerepos'
    id = Column(Integer, primary_key=True)
    imageurl = Column(String(), nullable= True)
    imagetag = Column(String(), nullable=True)

