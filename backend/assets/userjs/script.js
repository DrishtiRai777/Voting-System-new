var email=document.forms['form'][email];
var email_error=document.getElementById('email_error');
email.addEventListener('textInput',email_verify);
function validated(){
    if(email.value.length<9){
        email.style.border="1px solid red";
        email_error.style.display="block";
        email.focus();
        return false;
    }
}
function email_verify(){
    if(email.value.length>=8){
        email.style.border="1px solid silver";
        email_error.style.display="none";
        return true;
    }
}
