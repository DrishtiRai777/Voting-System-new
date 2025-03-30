document.getElementById('prevButton').addEventListener('click', function() {
    window.location.href = '/sign_up';
});

document.getElementById('nextButton').addEventListener('click', function(event) {
    if (validateForm()) {
        window.location.href = '/sign_up03';
    }
});


function clearErrors(){
    let errors = document.getElementsByClassName('formerror');
    for (let item of errors) {
        item.innerHTML = "";
    }
}

function setError(id, error) {
    let errorSpan = document.getElementById(id);
    if (errorSpan) {
        errorSpan.innerHTML = error;
    }
}

function validateForm() {
    let returnVal = true;
    clearErrors();

    // Admin Name validation
    let adminName = document.forms['myForm']["adminName"].value;
    if (adminName.length < 3) {
        setError('adminNameError', "*Name must be at least 3 characters");
        returnVal = false;
    }

    // DOB validation
    let dob = document.forms['myForm']["dob"].value;
    if (!dob) {
        setError('dobError', "*Date of birth is required");
        returnVal = false;
    }

    // Gender validation
    let gender = document.forms['myForm']["gender"].value;
    if (gender === "") {
        setError('genderError', "*Gender is required");
        returnVal = false;
    }

    // Institution Name validation
    let clgName = document.forms['myForm']["clgName"].value;
    if (clgName.length < 3) {
        setError('clgNameError', "*Institution name must be at least 3 characters");
        returnVal = false;
    }

    // Branch validation
    let branch = document.forms['myForm']["branch"].value;
    if (branch.length < 3) {
        setError('branchError', "*Branch name must be at least 3 characters");
        returnVal = false;
    }

    // College ID validation
    let clgId = document.forms['myForm']["clgId"].value;
    if (clgId.length < 6) {
        setError('clgIdError', "*College ID must be at least 6 characters");
        returnVal = false;
    }

    // Phone number validation
    let phNum = document.forms['myForm']["phNum"].value;
    if (phNum.length < 10) {
        setError('phNumError', "*Phone number must be at least 10 digits");
        returnVal = false;
    }

    // Email validation
    let email = document.forms['myForm']["email"].value;
    let emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    if (!emailPattern.test(email)) {
        setError('emailError', "*Please enter a valid email address");
        returnVal = false;
    }

    // Position validation
    let position = document.forms['myForm']["position"].value;
    if (position === "") {
        setError('positionError', "*Position is required");
        returnVal = false;
    }

    // Secretary Name validation
    let secName = document.forms['myForm']["secName"].value;
    if (secName.length < 3) {
        setError('secNameError', "*Secretary name must be at least 3 characters");
        returnVal = false;
    }

    // Secretary Phone Number validation
    let phoneNum = document.forms['myForm']["phoneNum"].value;
    if (phoneNum.length < 10) {
        setError('phoneNumError', "*Secretary phone number must be at least 10 digits");
        returnVal = false;
    }

    // Secretary Email validation
    let secEmail = document.forms['myForm']["secEmail"].value;
    if (!emailPattern.test(secEmail)) {
        setError('secEmailError', "*Please enter a valid email address");
        returnVal = false;
    }

    // Team Member Name validation
    let tmName1 = document.forms['myForm']["tmName"].value;
    if (tmName1.length < 3) {
        setError('tmName1Error', "*Team member name must be at least 3 characters");
        returnVal = false;
    }

    // Team Member Phone Number validation
    let tmPhoneNum1 = document.forms['myForm']["tmPhoneNum"].value;
    if (tmPhoneNum1.length < 10) {
        setError('tmPhoneNum1Error', "*Team member phone number must be at least 10 digits");
        returnVal = false;
    }

    // Team Member Email validation
    let tmEmail1 = document.forms['myForm']["tmEmail"].value;
    if (!emailPattern.test(tmEmail1)) {
        setError('tmEmail1Error', "*Please enter a valid email address");
        returnVal = false;
    }

    return returnVal;
}