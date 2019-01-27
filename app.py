import os
from flask import Flask, render_template, flash, redirect, request, url_for, session, make_response, current_app
from flask_pymongo import PyMongo
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = "whatthefuck"

app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = 'mongodb://admin:admin1@ds111425.mlab.com:11425/cookbook'

mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/breakfast')
def breakfast():
    return render_template('breakfast.html',
                            meals=mongo.db.meals.find())

@app.route('/dinner')
def dinner():
    return render_template('dinner.html',
                            meals=mongo.db.meals.find())

@app.route('/dessert')
def dessert():
    return render_template('dessert.html',
                            meals=mongo.db.meals.find())

@app.route('/login', methods=["POST", "GET"])
def login():
    users = mongo.db.users
    login_user = users.find_one({"username" : request.form.get("username", False)})
    if login_user:
        if (request.form['pass']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return 'Invalid username/password combination'

    return render_template('login.html')

@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        users = mongo.db.users
        existing_user = users.find_one({"username" : request.form['username']})
        if existing_user is None:
            users.insert({'username' : request.form['username'],
                            'password' : request.form['pass'],
                            'email' : request.form['email']
            })
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return "Username already exist"
    return render_template('register.html')
    
@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html')
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)