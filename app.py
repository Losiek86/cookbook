import os
from flask import Flask, render_template, flash, redirect, request, url_for, session, make_response, current_app

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/breakfast')
def breakfast():
    return render_template('breakfast.html')

@app.route('/dinner')
def dinner():
    return render_template('dinner.html')

@app.route('/dessert')
def dessert():
    return render_template('dessert.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)