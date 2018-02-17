#!/usr/bin/python
# -*- encoding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import thermometer
import date_and_time
import control_of_the_boiler_room

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

boil=0

def the_state_of_the_heating_system():
 global boil
 date_and_time.read_time()
 if GPIO.input(7)==0: 
  print ("Čerpadlo je zapnuto.")
 else:
  print ("Čerpadlo je vypnuto.")
 if boil == 0:
  print  ("Bojler je uzavřen.")
 else:
  print ("Bojler je otevřen.")

 t6 = thermometer.read_temp(6)
 t14 = thermometer.read_temp(14)

 print ("Teplota vody v bojleru je %s °C." %t6)
 print ("Teplota kolektoru je %s °C" %t14)
 print ("***************************************************************************")

t6 = thermometer.read_temp(6)
t14 = thermometer.read_temp(14)
while True:
 if (t14>=(t6+5)):
  pump_boil.open()
  boil=servo_boil.open(100)
  pump_boil.on()
  the_state_of_the_heating_system()
  while (t14>=(t6+5)):
   time.sleep(200)
   t6 = thermometer.read_temp(6)
   t14 = thermometer.read_temp(14)
 else:
  pump_boil.close()
  boil=servo_boil.open(0)
  pump_boil.off()
  the_state_of_the_heating_system()
  while (t14<(t6+5)):
   time.sleep(200)
   t6 = thermometer.read_temp(6)
   t14 = thermometer.read_temp(14)
