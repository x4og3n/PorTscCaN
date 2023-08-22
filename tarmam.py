#!/usr/bin/env python
# -*- coding : utf-8 -*-
 
import os
import nmap

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet port scan by xtogen")

print("""
xais olunur bir nov scan secesiniz

1) suretli scan
2) servis ve versiya scani
3) emeliyat sistemi melumatlnadirma
""")

islemno = input("istifade nomresini gir:")

if(islemno == "1"):
        hedefip = input("hedef ip yazin : ")
        os.system("nmap " + hedefip)
elif(islemno == "2"):
        hedefip = input("hedef ip yazin : ")
        os.system("nmap -sS -sV " + hedefip)
elif(islemno == "3"):
        hedefip = input("hedef ip yazin")        
        os.system("nmap -O " + hedefip)
else:
        print("sehvlik oldu program baglanilir")
