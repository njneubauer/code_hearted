from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

def calc_death_probability(data):
    model = joblib.load("simple_model.sav")
    return model.predict_proba(data)

def calc_death_probability(clinical_data):
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
    
    prob_clinical = calc_death_probability(clinical_data)

    print(f'Result: {prob_clinical[0][0]}')

    return render_template('clinical_calc.html', clinical_data=clinical_data, prob_clinical = prob_clinical)

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

    print(data)

    prob = calc_death_probability(data)

    print(f'Result: {prob[0][0]}')
    
    #Plug  Machine learning values to send to a results.html screen
    return render_template('patient_calc.html', data=data, prob=prob)


if __name__ == "__main__":
    app.run(debug=True)