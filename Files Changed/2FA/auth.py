import random
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('sender@gmail.com', 'app_password')
otp = ''.join([str(random.randint(0, 9)) for i in range(4)])
msg = "Your OTP is: " + otp
server.sendmail('sender@gmail.com', 'receiver@gmail.com', msg)
server.quit()
