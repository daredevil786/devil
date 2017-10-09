from gpiozero import MotionSensor

def mypic():
    import os
    import time
    a=0
    b=1
    while a<=10:

        t="fswebcam -F 5 --fps 20 -r \"1200x800\" /home/pi/cam/imgs/"+str(b)+".jpg"
        os.system(t)
        print(b)
        a=a+1
        b=b+1
        time.sleep(30)



def mytweet():
    from TwitterAPI import TwitterAPI

    CONSUMER_KEY = 'eDWLh4zSdo5SIFMNM6CxebAQ7'
    CONSUMER_SECRET = 'Vom9W8K5KX1VKTqKGPzPNF5XYEvFeBuR4GprF5lTIZAQbQ0qqP'
    ACCESS_TOKEN_KEY = '823063147712020481-MS9kF7Hm1fc3TjNm6NbaDNrfbIqX6O9'
    ACCESS_TOKEN_SECRET = 'RMkdy5xS27Y0t0E8gkmnH8CGFu4jW5K2Dri1EBDTcASte'
    b=1

    while True:
        b=b+1
        api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
        file = open('/home/pi/cams/imags/'+str(b)+'.jpg', 'rb')
        print('done')
        data = file.read()
        r = api.request('statuses/update_with_media', {'status':'#pyTweetCMR'}, {'media[]':data})
        print(r.status_code)    


pir = MotionSensor(4)
while True:
    if pir.motion_detected:
        print("Motion detected!")
        mypic()
        mytweet()
        

   
