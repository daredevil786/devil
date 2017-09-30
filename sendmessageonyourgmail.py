#!/usr/bin/python3
import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)	
s.starttls()
s.login("rudratheburningfire@gmail.com","9097362269")
message="yo"
s.sendmail("rudratheburningfire@gmail.com@gmail.com","rudratheburningfire@gmail.com",message)
s.quit()
