import random


from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from forms import RegisterForm
from models import db, Users
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash 



app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mi_database_users.db'
db.init_app(app)





@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('ok')


@app.route('/register/', methods= ['GET','POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data
        password = generate_password_hash(password)
        users = Users(first_name = first_name, last_name = last_name, email = email, password = password)
        db.session.add(users)
        db.session.commit()
        return f'вы зарегистрированы'
    return render_template('register.html', form = form)


@app.route('/users/', methods= ['GET','POST'])
def get_users():
    users = Users.query.all()
    print(list(users))
    return f'{list(users)}'