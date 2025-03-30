document.getElementById('submitButton').addEventListener('click', function() {
    if (validateForm()) {
        window.location.href = '/sign_up02';
    }
});

function clearErrors() {
    const errors = document.getElementsByClassName('formerror');
    for (let item of errors) {
        item.innerHTML = "";
    }
}

function setError(id, error) {
    let element = document.getElementById(id);
    let formErrorSpan = element ? element.querySelector('.formerror') : null;
    
    if (formErrorSpan) {
        formErrorSpan.innerHTML = error;
    }
}

function validateForm() {
    let returnVal = true;
    clearErrors();

    // Validate Organization Name
    let orgName = document.forms['myForm']["orgName"].value;
    if (orgName === "") {
        setError('orgNameError', "*Organization Name is required");
        returnVal = false;
    } else if (orgName.length < 3 || orgName.length > 50) {
        setError('orgNameError', "*Organization Name must be between 3 and 50 characters");
        returnVal = false;
    }

    // Validate Organization Address
    let orgAddress = document.forms['myForm']["orgAddress"].value;
    if (orgAddress === "") {
        setError('orgAddressError', "*Organization Address is required");
        returnVal = false;
    } else if (orgAddress.length < 10 || orgAddress.length > 100) {
        setError('orgAddressError', "*Address must be between 10 and 100 characters");
        returnVal = false;
    }

    // Validate Organization Contact Person
    let orgContactPerson = document.forms['myForm']["orgContactPerson"].value;
    if (orgContactPerson === "") {
        setError('orgContactPersonError', "*Organization Contact Person is required");
        returnVal = false;
    } else if (orgContactPerson.length < 3) {
        setError('orgContactPersonError', "*Contact Person must be at least 3 characters");
        returnVal = false;
    }

    // Validate Organization Email
    let orgEmail = document.forms['myForm']["orgEmail"].value;
    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if (orgEmail === "") {
        setError('orgEmailError', "*Organization Email is required");
        returnVal = false;
    } else if (!emailRegex.test(orgEmail)) {
        setError('orgEmailError', "*Invalid email format");
        returnVal = false;
    }

    return returnVal;
}