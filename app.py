from flask import Flask, request, render_template
import requests
## other dependencies
# import numpy as np
# import pickle

# Create instance of Flask
app = Flask(__name__)

option = request.form['customRadioInLine1']
# Establish connection to machine learning
# model = 

# Route to render html
@app.route("/")
def home():
    return render_template('index.html')

@app.route('/input')
def clinical_input():
    return option
    