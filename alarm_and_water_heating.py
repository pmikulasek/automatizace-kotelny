#!/usr/bin/python
# -*- encoding: utf-8 -*-
import RPi.GPIO as GPIO
import pump_boil
import servo_boil
import siren
import thermometer
import time

stop=0
j=0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.output(24, True)

j=0
k=0

while True:
 t1 = thermometer.read_temp(1)    #atmos
 t7 = thermometer.read_temp(7)    #boil
 t11 = thermometer.read_temp(11)  #storage tank
 t15 = thermometer.read_temp(15)  #temperature in boil room

 if ((t7>=40) and (j==0)):
  siren.signal()
  j=j+1
 elif ((t7<40) and (j==1)):
  j=j-1
 elif t15>=50:
  while True:
   siren.SOS()
 elif ((t1>=75) and (t7<50) and (k==0)):
  pump_boil.open()
  servo_boil.open(20)
  pump_boil.on()
  k=k+1
 elif (((t1<70) or (t7>60)) and (k==1)):
  pump_boil.off()
  servo_boil.open(0)
  pump_boil.close()
  k=k-1
 else:
  time.sleep(150)
