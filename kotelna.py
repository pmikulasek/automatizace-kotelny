#!/usr/bin/python
# -*- encoding: utf-8 -*-
import RPi.GPIO as GPIO
from Tkinter import *
import time
import teplomer
import datum_a_cas

master = Tk()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.output(8, True)
GPIO.output(9, True)
GPIO.output(10, True)
GPIO.output(17, True)
GPIO.output(18, True)

bojler=0

def zapni_cerpadlo():
 cekani()
 GPIO.output(8, False)
 stav_topne_soustavy()

def vypni_cerpadlo():
 cekani()
 GPIO.output(8, True)
 stav_topne_soustavy()

def otoc_trojcestnym_ventilem():
 otoceni=procento.get()
 otoceni=int(otoceni)
 cekani()
 if otoceni==100:
  GPIO.output(9, False)
  GPIO.output(10, False)
  master.after(150000)
  GPIO.output(9, True)
  GPIO.output(10, True)
 else:
  GPIO.output(9, False)
  master.after(150000) #uzavření ventilu
  time2=otoceni/10*15*1000
  GPIO.output(10, False)
  master.after(time2) #otevření ventilu na požadované procento
  GPIO.output(9, True)
  GPIO.output(10, True)
 stav_topne_soustavy()

def otevri_bojler():
 global bojler
 cekani()
 GPIO.output(17, False)
 GPIO.output(18, False)
 master.after(150000)
 GPIO.output(17, True)
 GPIO.output(18, True)
 if bojler % 2 == 0:
  bojler=bojler+1
 stav_topne_soustavy()

def zavri_bojler():
 global bojler
 cekani()
 GPIO.output(17, False)
 master.after(150000)
 GPIO.output(17, True)
 if bojler % 2 == 1:
  bojler=bojler+1
 stav_topne_soustavy()

def stav_topne_soustavy():
 datum_a_cas.read_cas()
 if GPIO.input(8)==0: #jesliže zjišťujeme stav pinu, musí zde být GPIO.input, i když je 8 pin výstupní
  print ("Čerpadlo je zapnuto.")
 else:
  print ("Čerpadlo je vypnuto.")
 print ("Trojcestný ventil je otevřen na %s procent." % procento.get())
 if bojler % 2 == 0:
  print  ("Bojler je uzavřen.")
 else:
  print ("Bojler je otevřen.")
  t1 = teplomer.read_temp(1)
 t2 = teplomer.read_temp(2)
 t3 = teplomer.read_temp(3)
 t4 = teplomer.read_temp(4)
 t5 = teplomer.read_temp(5)
 t6 = teplomer.read_temp(6)
 t7 = teplomer.read_temp(7)
 t8 = teplomer.read_temp(8)
 t9 = teplomer.read_temp(9)
 t10 = teplomer.read_temp(10)
 print ("Výstupní teplota z nádrží = zpáteční voda do kolektoru je %s °C." %t1)
 print ("Topná voda do domu (případně bojleru) = topná voda z kolektoru je %s °C." %t2)
 print "Vracející se voda z bojleru, popř. z domu je %s °C." %t3
 print "Teplota vody v bojleru je %s °C." %t4
 print "Zpátečka z akumulačních nádrží u kotle má %s °C" %t5
 print "Teplota kolektoru je %s °C" %t6
 print "Teplota kotle je %s °C" %t7
 print "Topná voda do nádrží má %s °C" %t8
 print "Akumulační nádrž nahoře má %s °C" %t9
 print "Teplota akumulační nádrže téměř dole je %s °C." %t10
 print "***************************************************************************"


#def radek(rodic, text, **parametry):#zde začíná vstupní pole
#    stitek=Label(rodic, text=text).pack()
#    vstup=Entry(rodic, **parametry)
#    vstup.pack()
#    return vstup

def cekani():
 time=cas.get()
 if time=="":
  time=0
 else:
  time=float(time)
 time=time*3600000
 time=int(time)
 master.after(time)

Button(master, text="Zapni čerpadlo", activebackground="red", font=("Arial",20,"bold"), command=zapni_cerpadlo).pack()  #upravit podle tohoto

c = Button(master, text="Vypni čerpadlo", activebackground="blue", font=("Arial",20,"bold"), command=vypni_cerpadlo)
c.pack()

d = Button(master, text="Otoč trojcestným ventilem", activebackground="red", font=("Arial",20,"bold"), command = otoc_trojcestnym_ventilem) #pokud chceme volat fci s p$
d.pack()

#vstup = Entry(master) #zde začíná vstupní pole
#vstup.pack()
#vstup.focus_set() #zde končí, v kódu je příkaz vstup.get(), který navrací vloženou hodnotu jako string


procento = StringVar()
Label(master, text="0% zavřeno - 100% otevřeno").pack()
Entry(master, textvariable=procento).pack()

cas = StringVar()
Label(master, text="Za jak dlouho akci provést? Zadejte čas v hodinách.").pack()
Entry(master, textvariable=cas).pack()

#procento=radek(master, u"0% zavřeno - 100% otevřeno")
#cas=radek(master, u"Za jak dlouho akci provést? Zadejte čas v hodinách.")

e = Button(master, text="Otevři bojler", activebackground="red", font=("Arial",20,"bold"), command=otevri_bojler)
e.pack()

f = Button(master, text="Zavři bojler", activebackground="blue", font=("Arial",20,"bold"), command=zavri_bojler)
f.pack()

g = Button(master, text="Vypiš stav topné soustavy", font=("Arial",20,"bold"), command = stav_topne_soustavy)
g.pack()

mainloop()
