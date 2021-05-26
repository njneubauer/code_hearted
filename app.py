from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

def calc_death_probability(data):
    model = joblib.load("simple_model.sav")
    return model.predict(data)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/clinical')
def clinical():
    return render_template('clinical_calc.html')

@app.route('/patient')
def patient():
    return render_template('patient_calc.html')

@app.route('/data', methods=['GET','POST'])
def search():
    age = request.form['age']
    sex = request.form['sex']
    smoker = request.form['smoking']
    anaemia = request.form['anaemia']   
    diabetes = request.form['diabetes'] 
    highbp = request.form['high_blood_pressure']
   

    dict = {'age': age, 'anaemia': anaemia, 'diabetes': diabetes, 'high_blood_pressure': highbp, 'sex': sex, 'smoking': smoker}
    
    data = pd.DataFrame(dict)
    
    
    # print(f"=======================")
    # # print(f"age={age}  gender={gender}  smoker={smoker}")
    # print(f"anemic={anemic}  diabetic={diabetic}  highbp={highbp}")
    # print(f"=======================")
    
    # Call to Machine Language 
    # Return information back from Machine Language 

    prob = calc_death_probability(data)

    #Plug  Machine learning values to send to a results.html screen
    return render_template('patient_calc.html', data=data, prob=prob)

if __name__ == "__main__":
    app.run(debug=True)