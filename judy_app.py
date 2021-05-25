from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('patient_calc.html')

@app.route('/patient_data', methods=['POST'])
def search():
    age = request.form['age']
    gender = request.form['gender']
    smoker = request.form['smoker']
    anemic = request.form['anemic']   
    diabetic = request.form['diabetic'] 
    highbp = request.form['highbp']
    
    print(f"=======================")
    print(f"age={age}  gender={gender}  smoker={smoker}")
    print(f"anemic={anemic}  diabetic={diabetic}  highbp={highbp}")
    print(f"=======================")
    
    # Call to Machine Language 
    # Return information back from Machine Language 

    #Plug  Machine learning values to send to a results.html screen
    return render_template('results.html',  age=age, gender=gender, 
                                            smoker=smoker, anemic=anemic, 
                                            diabetic=diabetic, highbp=highbp)

if __name__ == "__main__":
    app.run(debug=True)