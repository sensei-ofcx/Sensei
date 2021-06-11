#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time

os.system("pip install nslookup")
os.system("apt install nmap -y")
os.system("clear")

#Birinci Banner
banner = """
 	  	 ____                      _ 
		/ ___|  ___ _ __  ___  ___(_)
 		\___ \ / _ \ '_ \/ __|/ _ \ |
		 ___) |  __/ | | \__ \  __/ |
		|____/ \___|_| |_|___/\___|_|"""
#Secenek Ana kısım Burası
secenek = """
┌───────────────────────────────────────────────────────────┐
|		         Sensei   		 	    |
|            	    Coded by /Sensei                        |
|                                         		    |
|1=>Nmap Taramaları		2=>Whois, Ve Site ip Sorgusu|
|                                                           |
|3=>Kalan İşlemler		4=>Çıkış                    |
|                                                           |
|                                                           |
└───────────────────────────────────────────────────────────┘
"""
#nmap taramasında gözükecek yer
figlet = """
 	  	 ____                      _ 
		/ ___|  ___ _ __  ___  ___(_)
 		\___ \ / _ \ '_ \/ __|/ _ \ |
		 ___) |  __/ | | \__ \  __/ |
		|____/ \___|_| |_|___/\___|_|"""
banner2 = """
┌─────────────────────────────────────────────────────┐
|                        Sensei                       |
|                   Coded by /Sensei                  |
|                                                     |
|1=>Normal Tarama             		2=>Orta Tarama|
|                                                     |
|3=>Büyük Tarama              		4=>Çıkış      |
|                                                     |
|                                                     |
└─────────────────────────────────────────────────────┘

"""
#Whois Fln Kısmı
figlet2 = """
 	  	 ____                      _ 
		/ ___|  ___ _ __  ___  ___(_)
 		\___ \ / _ \ '_ \/ __|/ _ \ |
		 ___) |  __/ | | \__ \  __/ |
		|____/ \___|_| |_|___/\___|_|"""
banner3 = """
┌─────────────────────────────────────────────────────┐
|                        Sensei                       |
|                   Coded by /Sensei                  |
|                                                     |
|1=>Whois Taraması             		2=>Site İp Bul|
|                                                     |
|3=>Ping Atma              		4=>Çıkış      |
|                                                     |
|                                                     |
└─────────────────────────────────────────────────────┘

"""
#Kalan İşlemler Kısmı
figlet3 = """
 	  	 ____                      _ 
		/ ___|  ___ _ __  ___  ___(_)
 		\___ \ / _ \ '_ \/ __|/ _ \ |
		 ___) |  __/ | | \__ \  __/ |
		|____/ \___|_| |_|___/\___|_|"""
banner4 = """
┌─────────────────────────────────────────────────────┐
|                        Sensei                       |
|                   Coded by /Sensei                  |
|                                                     |
|1=>Admin Panel Finder                 	2=>Kurulumlar.|
|                                                     |
|3=>İndex Yapma              		4=>Çıkış      |
|                                                     |
|                                                     |
└─────────────────────────────────────────────────────┘

"""
print(banner)
print(secenek)

secim = input("/==>")
#nmap kısmı
if secim == "1":
	os.system("clear")
	print(figlet)
	print(banner2)
	secimnmap = input("/==>")
	if secimnmap == "1":
		Hedefsite = input("Hedef Site/==> ")
		os.system("nmap "+Hedefsite)
	elif secimnmap == "2":
		Hedefsite2 = input("Hedef Site/==> ")
		os.system("nmap -v -A "+Hedefsite2)
	elif secimnmap == "3":
		Hedefip = input("Hedef İp/==> ")
		os.system("nmap -v -sn "+Hedefip)
	elif secimnmap == "4":
		os.system("clear")
		exit()
#whois kısmı
elif secim == "2":
	os.system("clear")
	print(figlet2)
	print(banner3)
	secimwip = input("/==>")
	if secimwip == "1":
		Hedefsitewip = input("Hedef Site/==> ")
		os.system("whois "+Hedefsitewip)
	elif secimwip == "2":
		Hedefsitewip2 = input("Hedef Site/==> ")
		os.system("nslookup "+Hedefsitewip2)
	elif secimwip == "3":
		Hedefsitewip3 = input("Hedef İp/==> ")
		os.system("clear")
		os.system("ping "+Hedefsitewip3)
	elif secimwip == "4":
		os.system("clear")
		exit()
elif secim == "3":
	os.system("clear")
	print(figlet3)
	print(banner4)
	sec = input("/==>")
	if sec == "1":
		os.system("git clone https://github.com/saepsh/saepapf")
		os.chdir("saepapf")
		os.system("python2 saepapf.py")
		exit()
	elif sec == "2":
		os.system("clear")
		os.system("pkg install figlet -y")
		os.system("apt install figlet -y")
		os.system("apt install ruby -y")
		os.system("clear")
		os.system("pkg install git -y")
		os.system("pkg  update -y")
		os.system("apt update -y")
		os.system("pkg  upgrade -y")
		os.system("pkg install python3 -y")
		os.system("pkg install python2 -y")
		os.system("pkg  install git -y")
		os.system("pkg  install ninja -y")
		os.system("pkg install apt -y")
		os.system("apt install hydra -y")
		os.system("apt install unzip -y")
		os.system("apt install nmap -y")
		os.system("apt install termux-tools -y")
		os.system("pkg install curl -y")
		os.system("pkg install wget -y")
		os.system("pkg install pip -y")
		os.system("pkg install pip2 -y")
		os.system("pip install wordlist -y")
		os.system("pkg install nmap -y")
		os.system("pkg install hydra -y")
		os.system("pkg install sqlmap -y")	
		os.system("pkg install openssl -y")
		os.system("apt install nodejs -y")
	elif sec == "3":
		os.system("git clone https://github.com/4L13199/LITESCRIPT")
		os.chdir("LITESCRIPT")
		os.system("python2 LITESCRIPT.py")
		exit()
	elif sec == "4":
		os.system("clear")
		exit()
elif secim == "4":
	os.system("figlet Byy Byy")
	time.sleep(4)
	os.system("clear")
	exit()
else:
	print("Yanlış seçim")