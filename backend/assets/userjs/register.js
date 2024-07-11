const username=document.getElementById('username');
const email=document.getElementById('email');
const password=document.getElementById('password');
const confirmpassword=document.getElementById('confirmpassword');
const form=document.getElementById('form');
const contact=document.getElementById('contact');
const date=document.getElementById('date');
const name_error=document.getElementById('name_error');
const email_error=document.getElementById('email_error');
const password_error=document.getElementById('password_error');
const confirmpassword_error=document.getElementById('confirmpassword_error');
const contact_error=document.getElementById('contact_error');
const date_error=document.getElementById(date_error);


form.addEventListener('submit',(e)=>{
  var email_check= /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/
  if(username.value==='' || username.value==null)
  {
    e.preventDefault();
    name_error.innerHTML("Name is required");
  }
  if(username.value<=5){
    e.preventDefault();
    name_error.innerHTML="username must be more than five characters";
  }
  if(!email.value.match(email_check)){
    e.preventDefault();
    email_error.innerHTML="valid email is required";
  }
  if(password.value.length<=5){
    e.preventDefault();
    password_error.innerHTML="Password must be more than 6 characters long";
  }
  if(confirmpassword.value===''){
    e.preventDefault();
    confirmpassword_error.innerHTML="Password must be 6 characters long";
  }
  if(confirmpassword.value<=5){
    e.preventDefault();
    confirmpassword_error.innerHTML="Confirm password must be 6 characters long"
  }
  if(password.value !== confirmpassword.value){
    e.preventDefault();
    showError("password does not match");
  }
  if(contact.length>10){
    e.preventDefault();
    contact_error.innerHTML="Phone number cannot be greate than 10-digit";
  }
  if(contact.length<9){
    e.preventDefault();
    contact_error.innerHTML="Phone number must be a 10-digit number";
  }
  const dob=new Date(date.value);
  if(isNaN(dob.getTime()) && dob>new Date()){
    e.preventDefault();
    date_error.innerHTML="Please enter a valid date";
  }
})

