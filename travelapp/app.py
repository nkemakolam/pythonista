from flask import Flask, render_template

app = Flask(__name__)

#Defining the root of the app
@app.route("/")
def index():
    return "<h1> hello world</h1>"
#Defining the about Page
@app.route("/about")
def about():
    return "<h1> hello world about</h1>"

# returning the Contact us page
@app.route("/contact")
def contact():
    return "<h1> hello world Contact</h1>"