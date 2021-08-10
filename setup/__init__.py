from flask import Flask
from db import db
from setup.config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)

app.config.from_pyfile('config.py')


@app.before_first_request
def create_tables():
    db.create_all()



