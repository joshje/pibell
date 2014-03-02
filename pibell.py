#!/usr/bin/env python
from twython import Twython
import RPi.GPIO as GPIO
import time
import config

# Doorbell pin
buttonPin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN)
twitter = Twython(config.api_key,config.api_secret,config.access_key,config.access_secret)

lastPressed = 0
while True:
    now = time.time()
    if (GPIO.input(buttonPin) and (now - lastPressed > config.minInt)):
        lastPressed = now
        status = ''
        if (config.mentions): status += ' '.join(config.mentions) + ' '
        status += 'hey, someone just rang your doorbell'
        print status
        # twitter.update_status(status=status)
    time.sleep(0.05)
