function clearErrors(){
    let errors = document.getElementsByClassName('formerror');
    for (let item of errors)
        item.innerHTML = "";
}

function seterror(id, error) {
    let element = document.getElementById(id);
    let formErrorSpan = element.querySelector('.formerror');
    
    if (formErrorSpan) {
        formErrorSpan.innerHTML = error;
    }
}

function validateForm() {
    let returnVal = true;
    clearErrors();

    // Check email field 
    let email = document.forms['loginForm']["email"].value;
    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if (!emailRegex.test(email)) {
        seterror('emailError', "*Invalid email");
        returnVal = false;
    }

    // Check password field 
    let password = document.forms['loginForm']["pswd"].value;
    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    if (!passwordRegex.test(password)) {
        seterror('passwordError', "*Password must be 8+ chars, include a number, uppercase, and special character");
        returnVal = false;
    }

    return returnVal; 
}