from flask import render_template
import connexion

# Create the application instance
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('coffea.yml')

# Create a URL route in our application for "/"
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

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)