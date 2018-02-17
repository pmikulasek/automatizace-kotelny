#!/usr/bin/python
# -*- encoding: utf-8 -*-
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(8, GPIO.OUT)       # pump

def on():
 GPIO.output(8, False)

def off():
 GPIO.output(8, True)
