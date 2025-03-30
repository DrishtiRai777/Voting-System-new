import random
import string
import smtplib
from email.mime.text import MIMEText

# Function to generate a random verification code
def generate_verification_code(length=6):
    return ''.join(random.choices(string.digits, k=length))

# Function to send the verification email
def send_verification_email(to_email, verification_code):
    smtp_server = 'smtp.gmail.com'  # Replace with your SMTP server
    smtp_port = 587
    smtp_user = 'your_email@gmail.com'  # Replace with your email
    smtp_password = 'your_app_password'  # Replace with your app password or password

    subject = 'Your Verification Code'
    body = f'Your verification code is: {verification_code}'
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = smtp_user
    msg['To'] = to_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, to_email, msg.as_string())
        print(f"Verification email sent to {to_email}")
    except Exception as e:
        print(f"Error sending email: {e}")

# Function to verify the entered code with the sent code
def verify_code(input_code, actual_code):
    return input_code == actual_code

# Main function to handle the verification process
def main():
    user_email = input("Enter your email address: ")
    verification_code = generate_verification_code()  # Generate the code
    send_verification_email(user_email, verification_code)  # Send the code via email
    
    # Prompt the user to enter the code
    user_input = input("Enter the verification code sent to your email: ")
    
    if verify_code(user_input, verification_code):
        print("Verification successful!")
    else:
        print("Verification failed. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()

# Replace 'your_email@gmail.com' with the email address you want to use for sending the OTP.
# Replace 'your_app_password' with the app password if you're using Gmail with 2FA.
# Replace 'user@example.com' with the email address of the person you're sending the OTP to (this could also be dynamic, depending on the context).