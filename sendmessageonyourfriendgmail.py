#!/usr/bin/python3
import smtplib
s=smtplib.SMTP('smtp.gmail.com',587) #condition for sending mail	
s.starttls()
s.login("theprotectorofsword@gmail.com","9934816772") # write your gmail and password
message="hiiii rahul" #write message which you want to send
s.sendmail("theprotectorofsword@gmail.com","rudratheburningfire@gmail.com",message) # write your mail and your friend mail
s.quit()
