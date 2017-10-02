#!/usr/bin/python3
import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)	# condition for sending mail
s.starttls()
s.login("rudratheburningfire@gmail.com","9097362269") #write your gmail and password
message="yo" #write message
s.sendmail("rudratheburningfire@gmail.com@gmail.com","rudratheburningfire@gmail.com",message) #write gmail of sender and reciever
s.quit()
