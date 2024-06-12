from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import DateTime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mi_database_users.db'
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(80), nullable= False)
    last_name = db.Column(db.String(80), nullable= False)
    email  = db.Column(db.String(120), nullable= False)
    password = db.Column(db.String(80), nullable= False)


    def __repr__(self) -> str:
        return f'{self. first_name} {self.last_name } {self.email} {self.password}'