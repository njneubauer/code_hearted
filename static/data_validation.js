function data_validation() {
    var age = document.forms['form']['age'].value
    var gender = document.forms['form']['gender'].value
    var htn = document.forms['form']['hypertension'].value
    var smoker = document.forms['form']['smoker'].value
    var diabetes = document.forms['form']['diabetes'].value
    var anemia = document.forms['form']['anemia'].value
    var cp = document.forms['form']['creatine_phosphate'].value
    
    console.log(age)

    if(age == "" || age < 30 || age > 95){
        alert("Please enter an age between 30-95");
        return false;
    }

    if(!gender){
        alert("Please select a gender");
        return false;
    }

    if(!htn){
        alert("Please select a hypertension status");
        return false;
    }

    if(!smoker){
        alert("Please select a smoking status");
        return false;
    }

    if(!diabetes){
        alert("Please select a diabetes status");
        return false;
    }

    if(!anemia){
        alert("Please select a anemia status");
        return false;
    }

    if(cp == "" || cp >=0) {
        alert("Please enter an integer >0");
        return false;
    }
}