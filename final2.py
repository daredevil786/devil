
import RPi.GPIO as GPIO                    #Import GPIO library
import time
#Import time library
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)                    # programming the GPIO by BCM pin numbers
TRIG = 24
TRIG1 = 27
TRIG2 = 26
ECHO = 23
ECHO1 = 17
ECHO2 = 13
led = 19
m11=16
m12=12
m21=21
m22=20
GPIO.setup(TRIG,GPIO.OUT)                  # initialize GPIO Pin as outputs
GPIO.setup(TRIG1,GPIO.OUT) 
GPIO.setup(TRIG2,GPIO.OUT) 
GPIO.setup(ECHO,GPIO.IN)                   # initialize GPIO Pin as input
GPIO.setup(ECHO1,GPIO.IN) 
GPIO.setup(ECHO2,GPIO.IN)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(m11,GPIO.OUT)
GPIO.setup(m12,GPIO.OUT)
GPIO.setup(m21,GPIO.OUT)
GPIO.setup(m22,GPIO.OUT)
time.sleep(0.2)
def stop():
    print ("stop")
    GPIO.output(m11, 0)
    GPIO.output(m12, 0)
    GPIO.output(m21, 0)
    GPIO.output(m22, 0)
def forward():
    GPIO.output(m11, 1)
    GPIO.output(m12, 0)
    GPIO.output(m21, 1)
    GPIO.output(m22, 0)
    print ("Forward")
def back():
    GPIO.output(m11, 0)
    GPIO.output(m12, 1)
    GPIO.output(m21, 0)
    GPIO.output(m22, 1)
    print ("back")
def left():
    GPIO.output(m11, 0)
    GPIO.output(m12, 0)
    GPIO.output(m21, 1)
    GPIO.output(m22, 0)
    print ("left")
def right():
    GPIO.output(m11, 1)
    GPIO.output(m12, 0)
    GPIO.output(m21, 0)
    GPIO.output(m22, 0)
    print ("right")
stop()
count=0
while True:
 i=0
 avgDistance=0
 for i in range(15):
  GPIO.output(TRIG, False)                 #Set TRIG as LOW
  time.sleep(0.1)                                   #Delay
  GPIO.output(TRIG, True)                  #Set TRIG as HIGH
  time.sleep(0.00001)                           #Delay of 0.00001 seconds
  GPIO.output(TRIG, False)                 #Set TRIG as LOW
  while GPIO.input(ECHO)==0:              #Check whether the ECHO is LOW
       GPIO.output(led, False)             
  pulse_start = time.time()
  while GPIO.input(ECHO)==1:              #Check whether the ECHO is HIGH
       GPIO.output(led, False) 
  pulse_end = time.time()
  pulse_duration = pulse_end - pulse_start #time to get back the pulse to sensor
  distance = pulse_duration * 17150        #Multiply pulse duration by 17150 (34300/2) to get distance
  distance = round(distance,2)                 #Round to two decimal points
  avgDistance=avgDistance+distance
 avgDistance=avgDistance/5
 print ("avgDistance")
 flag=0
 if avgDistance < 150:      #Check whether the distance is within 15 cm range
    count=count+1
    stop()
    time.sleep(0.2)
    back()
    time.sleep(0.02)
    if (count%6 ==1) & (flag==0):
     right()
     flag=1
    else:
     left()
     flag=0
    time.sleep(0.2)
    stop()
    time.sleep(0.2)
 else:
    forward()
    flag=0
  
