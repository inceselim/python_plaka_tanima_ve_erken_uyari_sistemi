# -*- coding: utf-8 -*-
"""
Proje : Plaka tespit ve Erken uyarı sistemi
@author: Selim INCE
Note : 
#Program ilk çalıştırıldığında database_connect.py include edilip database oluşturulmalıdır...
"""
import plaka_tanima #plaka karakter tanima modulu
import sqlite3 #Database Module
import time
import telesign_module
import sys
from datetime import datetime

#Degiskenler-------------------------------------------------------------------
global sofor
global plakakarakter1
global plakakarakter2
#Database----------------------------------------------------------------------
dbconnect = sqlite3.connect('aracbilgi.db') #Database Connect Variable
dbconnect.row_factory = sqlite3.Row
database_select = dbconnect.cursor()  # Operation relation in Database

veribul=dbconnect.cursor()
veribul.execute('SELECT adsoyad FROM info')
#islem-------------------------------------------------------------------------
print ("Bilgilere Ulasiliyor ...")
for verisay in veribul.fetchall():
    sofor = verisay['adsoyad']
    print ("Araci sahibi bulundu : "+sofor)
    if (sofor):
        phone_number = "905374276035"
        taslak = "Sayin "+sofor + " 10sn. icersinde aracinizi bulundugu yerden aliniz..."
        message = (taslak)
        message_type = "ARN"
        messaging = MessagingClient(customer_id, api_key)
        response = messaging.message(phone_number, message, message_type)

        print ("Uyari mesaji gonderildi.")
        
        for i in reversed(range(0, 10)):
           time.sleep(1)
           print "%s\r" %i
        
#esleme_kontrol_---------------------------------------------------------------
        print ("Tarama yeniden baslatildi ...")
        print ("Tespit edilen plaka : "+plakakarakter2)
        
        if plakakarakter1==plakakarakter2:
            print ("Esleme yapildi.")
            taslak = "Sayin "+sofor + " ceza yediniz... "
            message = (taslak)
            message_type = "ARN"
            messaging = MessagingClient(customer_id, api_key)
            response = messaging.message(phone_number, message, message_type)
            print ("Arac sahibine bilgilendirme mesaji gonderildi...")
            
            ceza_tarih = str(datetime.now())
            ceza_kayitlari = open("ceza_kayitlari.txt","a")
            ceza_kayitlari.write(sofor + " " + plakakarakter1 + " " + ceza_tarih + "\n")
            ceza_kayitlari.close()
            print (ceza_tarih + " tarihli ceza kaydi olusturuldu.")
        else:
            print ("Eslesme bulunamadi program durduruluyor...")
#------------------------------------------------------------------------------       
dbconnect.commit() #veritabanı veriler işletildi
dbconnect.close() #veritabanı kapatıldı
#------------------------------------------------------------------------------
