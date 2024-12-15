#importing needed materials from flask module in order to create routes and the website itself
from flask import Flask, render_template, request, session, redirect
import sqlite3
import db

#Creates the Flask app
app = Flask(__name__)
app.secret_key = "rv"
#Route to Home Page
@app.route("/")
def Home():
    reviewData = db.GetAllReviews()
    return render_template("index.html", Reviewseview = reviewData)
#Route to Login Page 
@app.route("/login", methods=["GET", "POST"])
def Login():

 if request.method == "POST":
    username = request.form['username']
    password = request.form['password']

    user - db.CheckLogin(username, password)
    if user:
        session['id'] = user['id']
        session['username'] = username

        return redirect("/")

 return render_template("login.html")
#Route to Logout Page
 @app.route("/logout")
 def Logout():
    session.clear()
    return redirect("/")
#Route to Register Page
@app.route("/register", methods=["GET", "POST"])
def Register():

    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']


        if db.RegisterUser(username, password):

            return redirect("/")
        
    return render_template("register.html")

#Route in order to sign up/add as new user
@app.route("/add", methods=["GET","POST"])
def Add():

    if session.get('username') == None:
        return redirect("/")

    if request.method == "POST":
        user_id = session['id']
        date = request.form['date']
        moviegame = request.form['moviegame']
        score = request.form['score']

        db.AddReview(user_id, date, moviegame, score)

    return render_template("add.html")
        
#Directs user to the site (and debugs the site as well)
app.run(debug=True, port=8000)