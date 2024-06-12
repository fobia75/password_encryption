from wtforms import IntegerField, SelectField, StringField
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired ,Email, EqualTo

class RegisterForm(FlaskForm):
    first_name= StringField('first_name', validators= [DataRequired()])
    last_name= StringField('last_name', validators= [DataRequired()])
    email = StringField('email', validators= [DataRequired(), Email()]) 
    password = StringField('password',  validators= [DataRequired()])
    confirm_password = StringField('confirm_password',  validators= [DataRequired(), EqualTo('password')])
