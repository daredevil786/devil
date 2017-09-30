import os
import time

a=1
b=1

while a<15:
	img="fswebcam -F 3 --fps 25 -r 800x600 " + str(b)+".jpg"
	os.system(img)
	time.sleep(10)
	a=a+1
	b=b+1
