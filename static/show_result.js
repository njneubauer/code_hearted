function showResult(){
    console.log("function fired")
    var result = document.getElementById("myResult");
    console.log(result.style.display)
    if (result.style.display == "none"){
        result.style.display = "block";
    } 
}