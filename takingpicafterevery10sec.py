import os
import time

a=1
b=1

while a<15:
	img="fswebcam -F 3 --fps 25 -r 800x600 " + str(b)+".jpg" #conditon for run camera and it's quality
	os.system(img) 
	time.sleep(10) #condition for rum camera after every 10sec
	a=a+1
	b=b+1
