#!/usr/bin/python
# -*- encoding: utf-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(9, GPIO.OUT)       # servo three way valve
GPIO.setup(10, GPIO.OUT)      # servo three way valve

def open(x):
 if x==100:
  GPIO.output(10, False)
  time.sleep(150)
  GPIO.output(10, True)
 else:
  GPIO.output(9, False)
  time.sleep(150)            #close valve
  x=x/2*3
  GPIO.output(9, True)
  GPIO.output(10, False)
  time.sleep(x)              #opening the valve to the required percentage
  GPIO.output(10, True)
 return x

