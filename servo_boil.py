#!/usr/bin/python
# -*- encoding: utf-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)      # servo boil
GPIO.setup(18, GPIO.OUT)      # servo boil

def open(x):
 if x==100:
  GPIO.output(17, False)
  GPIO.output(18, False)
  time.sleep(150)
  GPIO.output(17, True)
  GPIO.output(18, True)
 else:
  GPIO.output(17, False)
  time.sleep(150) #close valve
  x=x/2*3
  GPIO.output(18, False)
  time.sleep(x) #opening the valve to the required percentage
  GPIO.output(17, True)
  GPIO.output(18, True)
 return x

