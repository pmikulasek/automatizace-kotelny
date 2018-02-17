#!/usr/bin/python
# -*- encoding: utf-8 -*-
import datetime
def read_time():
 dnes=datetime.datetime.now()
 if dnes.strftime("%a")=="Sat":
  den="sobota"
 elif dnes.strftime("%a")=="Sun":
  den="neděle"
 elif dnes.strftime("%a")=="Mon":
  den="pondělí"
 elif dnes.strftime("%a")=="Tue":
  den="úterý"
 elif dnes.strftime("%a")=="Wed":
  den="středa"
 elif dnes.strftime("%a")=="Thu":
  den="čtvrtek"
 elif dnes.strftime("%a")=="Fri":
  den="pátek"
 else:
  print("Nemůžu přeložit den do češtiny!")
 print("******************* Dnes je " + den + dnes.strftime(" %d-%m-%Y %H:%M") + " ***********************")

