from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/domov")
def home():
    return render_template("home.html")

@app.route("/nova-recenze")
def newReview():
    return render_template("review.html")

@app.route("/doporuceni")
def suggestions():
    return render_template("suggestions.html")

@app.route("/objevovani")
def exploration():
    return render_template("exploration.html")

@app.route("/moje-recenze")
def reviewList():
    return render_template("list.html")