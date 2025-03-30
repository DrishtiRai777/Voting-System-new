document.getElementById('prevButton').addEventListener('click', function() {
    window.location.href = '/sign_up02';
});
document.getElementById('submitButton').addEventListener('click', function(event) {
    if (validateForm()) {
        window.location.href = '/org_dashboard';
    }
});


function validateForm() {
    clearErrors();

    let isValid = true;

    // User name validation
    let user = document.getElementById("user").value;
    if (user.length < 3) {
        setError("userError", "*User name must be at least 3 characters");
        isValid = false;
    }

    // Password validation
    let pswd = document.getElementById("pswd").value;
    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    if (!passwordRegex.test(pswd)) {
        setError("pswdError", "*Password must be 8+ chars, include a number, uppercase, and special character");
        isValid = false;
    }

    // Confirm Password validation
    let cPswd = document.getElementById("c-pswd").value;
    if (pswd !== cPswd) {
        setError("cPswdError", "*Passwords do not match");
        isValid = false;
    }
    return isValid;
}

// Set error messages
function setError(id, message) {
    document.getElementById(id).innerText = message;
}

// Clear error messages
function clearErrors() {
    let errors = document.querySelectorAll(".formerror");
    errors.forEach(function(error) {
        error.innerText = "";
    });
}