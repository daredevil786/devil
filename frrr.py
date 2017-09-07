#!/usr/bin/python3
import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)	
s.starttls()
s.login("theprotectorofsword@gmail.com","9934816772")
message="yo"
s.sendmail("theprotectorofsword@gmail.com","theprotectorofsword@gmai.com",message)
s.quit()
