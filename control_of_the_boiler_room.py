#!/usr/bin/python
# -*- encoding: utf-8 -*-
import RPi.GPIO as GPIO
from Tkinter import *
import date_and_time
import pump_boil
import pump
import servo_boil
import siren
import thermometer
import three_way_valve
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.output(7, True)    # pump boil
GPIO.output(8, True)    # pump
GPIO.output(9, True)    # three way valve
GPIO.output(10, True)   # three way valve
GPIO.output(17, True)   # servo boil
GPIO.output(18, True)   # servo boil
GPIO.output(22, True)   # servo pump boil
GPIO.output(23, True)   # servo pump boil
GPIO.output(24, True)   # siren

master = Tk()

x=0
boil=0

def wait():
 time=cas.get()
 if time=="":
  time=0
 else:
  time=float(time)
 time=time*3600000
 time=int(time)
 master.after(time)

def switch_on_the_heating_with_a_pump():
 global x
 x=50
 wait()
 three_way_valve.open(x)
 pump.on()
 the_state_of_the_heating_system()

def switch_on_the_heating_without_a_pump():
 global x
 x=100
 wait()
 three_way_valve.open(x)
 the_state_of_the_heating_system()

def turn_off_the_heating():
 global x
 x=0
 wait()
 three_way_valve.open(x)
 pump.off()
 the_state_of_the_heating_system()

def the_state_of_the_heating_system():
 date_and_time.read_time()
 if GPIO.input(8)==0:                           #jesliže zjišťujeme stav pinu, musí zde být GPIO.input, i když je 8 pin výstupní
  print ("Čerpadlo je zapnuto.")
 else:
  print ("Čerpadlo je vypnuto.")
 print ("Trojcestný ventil je otevřen na %s procent." %x)
 if boil == 0:
  print  ("Bojler je uzavřen.")
 else:
  print ("Bojler je otevřen.")

def open_boil():
 global boil
 boil=servo_boil.open(100)
 the_state_of_the_heating_system()

def close_boil():
 global boil
 boil=servo_boil.open(0)
 the_state_of_the_heating_system()

def temperature():
 the_state_of_the_heating_system()
 t1 = thermometer.read_temp(1)
 t2 = thermometer.read_temp(2)
 t3 = thermometer.read_temp(3)
 t4 = thermometer.read_temp(4)
 t5 = thermometer.read_temp(5)
 t6 = thermometer.read_temp(6)
 t7 = thermometer.read_temp(7)
 t8 = thermometer.read_temp(8)
 t9 = thermometer.read_temp(9)
 t10 = thermometer.read_temp(10)
 t11 = thermometer.read_temp(11)
 t12 = thermometer.read_temp(12)
 t13 = thermometer.read_temp(13)
 #t14 = thermometer.read_temp(14)
 t15 = thermometer.read_temp(15)
 print ("Teplota kotle je %s °C." %t1)
 print ("PŘED trojcestným ventilem je %s °C." %t2)
 print ("ZA trojcestným ventilem je %s °C?" %t3)
 print ("POD trojcestným ventilem je %s °C." %t4)
 print ("Zpátečka z domu má %s °C." %t5)
 print ("Vstup do bojleru má %s °C." %t6)
 print ("Teplota vody v bojleru je %s °C." %t7)
 print ("Zpátečka z bojleru má %s °C." %t8)
 print ("Vstup do akumulačních nádrží má %s °C." %t9)
 print ("Zpátečka do akumulačních nádrží má %s °C?" %t10)
 print ("Akumulační nádrž nahoře má %s °C." %t11)
 print ("Akumulační nádrž téměř dole má %s °C." %t12)
 print ("Zpátečka z akumulačních nádrží má %s °C." %t13)
 #print ("Teplota kolektoru je %s °C." %t14)
 print ("Teplota u stropu je %s °C." %t15)
 print ("***************************************************************************")


a = Button(master, text="Zapni topení s čerpadlem", activebackground="red", font=("Arial",20,"bold"), command=switch_on_the_heating_with_a_pump)
a.pack()

b = Button(master, text="Zapni topení bez čerpadla", activebackground="red", font=("Arial",20,"bold"), command=switch_on_the_heating_without_a_pump)
b.pack()

c = Button(master, text="Vypni topení", activebackground="blue", font=("Arial",20,"bold"), command = turn_off_the_heating)
c.pack()

cas = StringVar()
Label(master, text="Za jak dlouho akci provést? Zadejte čas v hodinách.").pack()
Entry(master, textvariable=cas).pack()

e = Button(master, text="Otevři bojler", activebackground="red", font=("Arial",20,"bold"), command=open_boil)
e.pack()

f = Button(master, text="Zavři bojler", activebackground="blue", font=("Arial",20,"bold"), command=close_boil)
f.pack()

g = Button(master, text="Vypiš stav topné soustavy", font=("Arial",20,"bold"), command = temperature)
g.pack()

h = Button(master, text="Zatrub", font=("Arial",20,"bold"), command = siren.signal)
h.pack()

mainloop()
