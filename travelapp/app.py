from flask import Flask, render_template

app = Flask(__name__)

#Defining the root of the app
@app.route("/")
def index():
    return render_template("static/templates/master.html", message="this is the home")
#Defining the about Page
@app.route("/about")
def about():
    return render_template("static/templates/master.html", message="this is the about")
# returning the Contact us page
@app.route("/contact")
def contact():
     return render_template("static/templates/master.html", message="this is the contact")