import os, subprocess, time
import RPi.GPIO as GPIO

os.environ['DISPLAY'] = ":0"

PIR = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN)
displayison = False
maxidle = 10 # seconds
lastsignaled = 0
while True:
    now = time.time()
    if GPIO.input(PIR):
        if not displayison:
                subprocess.call('xset dpms force on', shell=True)
                subprocess.call('/opt/vc/bin/tvservice -p', shell=True)
                displayison = True
                lastsignaled = now
    else:
        if now-lastsignaled > maxidle:
            if displayison:
                subprocess.call('/opt/vc/bin/tvservice -o', shell=True)
                displayison = False
    time.sleep(1)
