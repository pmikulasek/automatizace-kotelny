#!/usr/bin/python
# -*- encoding: utf-8 -*-
import RPi.GPIO as GPIO
from Tkinter import *
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.OUT)      # siren

def SOS():
 for i in range(3):
  GPIO.output(24, False)
  time.sleep(2)
  GPIO.output(24, True)
  time.sleep(0.5)
 for i in range(3):
  GPIO.output(24, False)
  time.sleep(1)
  GPIO.output(24, True)
  time.sleep(0.5)
 for i in range(3):
  GPIO.output(24, False)
  time.sleep(2)
  GPIO.output(24, True)
  time.sleep(0.5)

def signal():
 for i in range(3):
  GPIO.output(24, False)
  time.sleep(1)
  GPIO.output(24, True)
  time.sleep(0.5)
