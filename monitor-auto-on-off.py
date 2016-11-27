import os, subprocess, time
import RPi.GPIO as GPIO

os.environ['DISPLAY'] = ":0"

PIR = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN)
displayison = False
maxidle = 2*60 # seconds
lastsignaled = 0
while True:
    now = time.time()
    if GPIO.input(PIR):
         lastsignaled = now
         if not displayison:
            subprocess.call('/opt/vc/bin/tvservice -p', shell=True)
            subprocess.call('xset dpms force on', shell=True)
            displayison = True
            print('Display on')
    else:
        if now-lastsignaled > maxidle:
            if displayison:
               subprocess.call('/opt/vc/bin/tvservice -o', shell=True)
               displayison = False
               print('Display off')
    time.sleep(1)
