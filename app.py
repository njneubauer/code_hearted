from flask import Flask, request, render_template
import requests
## other dependencies
# import numpy as np
# import pickle

# Create instance of Flask
app = Flask(__name__)
# option = request.form['customRadioInline1']

# Establish connection to machine learning
# model = 

# Route to render html
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/clinical_calc", methods=['GET'])
def clinical_input():
    option = request.form['customRadioInline1']
    return render_template("clinical_calc.html", option)



# @app.route("/clinical_calc.html")
# def clinical_input():
#     option = request.form['customRadioInline1']
#     print(option)
#     return option

if __name__ == "__main__":
    app.run(debug=True)    