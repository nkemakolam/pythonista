from flask import render_template
from flask import request
from app import app
from app import process_data

@app.route('/',methods=['GET'])
def index():
    return render_template("index.html",example=process_data.process())

@app.route('/covid',methods=['GET'])
def covid():
    return render_template("covid.html",cvd=process_data.covid_get())