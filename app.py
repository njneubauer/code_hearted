from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

def patient_death_probability(data):
    model = joblib.load("simple_model.sav")
    return model.predict_proba(data)

def clinical_death_probability(clinical_data):
    model = joblib.load("complex_model.sav")
    return model.predict_proba(clinical_data)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/clinical')
def clinical():
    return render_template('clinical_calc.html')

@app.route('/patient')
def patient():
    return render_template('patient_calc.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/clinical_data', methods=['GET','POST'])
def clinical_data():
    age = request.form['age']
    gender = request.form['gender']
    hypertension = request.form['hypertension']
    smoker = request.form['smoker']
    diabetes = request.form['diabetes']
    anemia = request.form['anemia']
    creatine = request.form['creatine_phosphate']
    ejection_fraction = request.form['ejection_fraction']
    platelets = request.form['platelets']
    sodium = request.form['sodium']
    office_vist = request.form['office_visit']
    
    
    clinical_data_dict = {'age':age, 'anemia':anemia, 'creatine_phosphokinase':creatine, 'diabetes':diabetes, 'ejection_fraction': ejection_fraction,'high_blood_pressure': hypertension, 
                        'platelets':platelets, 'serum_creatinine':creatine, 'serum_sodium':sodium, 'sex':gender, 'smoking':smoker, 'time':office_vist}

    clinical_data = pd.DataFrame(clinical_data_dict, index=[0])

    print(clinical_data)

    prob_clinical = np.round(clinical_death_probability(clinical_data) * 100, 2)

    return render_template('clinical_calc.html', input=clinical_data_dict, prob_clinical = prob_clinical[0][0])

@app.route('/patient_data', methods=['GET','POST'])
def search():
    age = request.form['age']
    sex = request.form['gender']
    smoker = request.form['smoker']
    anemia = request.form['anemic']   
    diabetes = request.form['diabetic'] 
    highbp = request.form['highbp']
    
    dict = {'age': [age], 'anaemia': [anemia], 'diabetes': [diabetes], 'high_blood_pressure': [highbp], 'sex': [sex], 'smoking': [smoker]}
    
    data = pd.DataFrame(dict)

    prob = np.round(patient_death_probability(data) * 100,2)

    patient_dict = {'age': age,  'sex': sex, 'smoker': smoker, 'anemia': anemia, 'diabetes': diabetes, 'highbp': highbp }
    print(patient_dict)

    return render_template('patient_calc.html', data=patient_dict, prob=prob[0][0])


if __name__ == "__main__":
    app.logger.addHandler(logging.StreamHandler(sys.stdout))
    app.logger.setLevel(logging.ERROR)
    app.run(debug=True)

