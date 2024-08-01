#code for otp verification

import smtplib

m=input("Please enter your email id: ")
#receiver address
print('Verify your account')

#A random OTP being generated
val= random.randint(1000,9999)

#Send OTP
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login('<sender address>','<sender email password ie.app password>')
    #NOTE: do note that you will not be able to log in using your email password.
    #You have to login using an app password set separately.
    
    subject = 'OTP Verification'
    body = 'The OTP to veriby you is ' + str(val)
    msg = f'Subject: {subject}\n\n{body}'
    smtp.sendmail('<sender address>',m,msg)

#Verify OTP
for a in range (1,5):
    ver=int(input('pls enter the opt you have received in your email: '))
    if ver == val:
        print("You have entered a correct otp")
        break
    else:
        print("it is not a correct opt you have entered")
        continue

