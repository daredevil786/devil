#!/usr/bin/python3
import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)	
s.starttls()
s.login("rudratheburningfire@gmail.com","tani23sharma24")
message="yo"
s.sendmail("tani23sharma23@gmail.com","tani23sharma23@gmail.com",message)
s.quit()
