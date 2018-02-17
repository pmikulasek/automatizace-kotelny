#!/usr/bin/python
# -*- encoding: utf-8 -*-
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(7, GPIO.OUT)       # pump boil
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

def on():
 GPIO.output(7, False)

def off():
 GPIO.output(7, True)

def open():
 GPIO.output(22, False)
 GPIO.output(23, False)
 time.sleep(150)
 GPIO.output(22, True)
 GPIO.output(23, True)

def close():
 GPIO.output(22, False)
 time.sleep(150)
 GPIO.output(22, True)
