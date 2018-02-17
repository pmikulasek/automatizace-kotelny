#!/usr/bin/python
# -*- encoding: utf-8 -*-
import os
import glob
import time
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'

def read_temp(i):
 if i==1:
  device_folder = glob.glob(base_dir + '28-04162253e7ff')[0]
 elif i==2:
  device_folder = glob.glob(base_dir + '28-0416859ab9ff')[0]
 elif i==3:
  device_folder = glob.glob(base_dir + '28-0517806418ff')[0]
 elif i==4:
  device_folder = glob.glob(base_dir + '28-041780e655ff')[0]
 elif i==5:
  device_folder = glob.glob(base_dir + '28-041780f414ff')[0]
 elif i==6:
  device_folder = glob.glob(base_dir + '28-05178024b1ff')[0]
 elif i==7:
  device_folder = glob.glob(base_dir + '28-0000079ba6d6')[0]
 elif i==8:
  device_folder = glob.glob(base_dir + '28-041685d8b3ff')[0]
 elif i==9:
  device_folder = glob.glob(base_dir + '28-041780ca9bff')[0]
 elif i==10:
  device_folder = glob.glob(base_dir + '28-05178035baff')[0]
 elif i==11:
  device_folder = glob.glob(base_dir + '28-0316224b7aff')[0]
 elif i==12:
  device_folder = glob.glob(base_dir + '28-0000079a3dae')[0]
 elif i==13:
  device_folder = glob.glob(base_dir + '28-0416220217ff')[0]
 elif i==14:
  device_folder = glob.glob(base_dir + '28-041621ed56ff')[0]
 elif i==15:
  device_folder = glob.glob(base_dir + '28-041780cac4ff')[0]
 else:
  print "Čísla teploměrů jsou od 1 do 15!"

 device_file = device_folder + '/w1_slave'
 a = open(device_file, 'r')
 lines = a.readlines()
 a.close()

 while lines[0].strip()[-3:] != 'YES':
  time.sleep(0.2)
  lines = read_temp_raw()
 equals_pos = lines[1].find('t=')
 if equals_pos != -1:
  temp_string = lines[1][equals_pos+2:]
  temp_c = float(temp_string) / 1000.0
 return temp_c
