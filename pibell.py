#!/usr/bin/env python
from twython import Twython
import RPi.GPIO as GPIO
import time
import random
import config

# Doorbell pin
buttonPin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN)
twitter = Twython(config.api_key,config.api_secret,config.access_key,config.access_secret)

messages = [
    'hey, someone just rang your doorbell',
    'ding dong, ding dong',
    'knock knock, who\'s there?',
    'yo, someone\'s at the door',
    'yo, the bell just went',
    'are you going to get that or shall I?'
]

def getStatusMessage():
    status = ''
    if (config.mentions): status += ' '.join(config.mentions) + ' '
    status += random.choice(messages)
    if (config.debug): print status
    else: twitter.update_status(status=status)

lastPressed = 0
while True:
    now = time.time()
    if (GPIO.input(buttonPin) and (now - lastPressed > config.minInt)):
        lastPressed = now
        getStatusMessage()
    time.sleep(0.05)
