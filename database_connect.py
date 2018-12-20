# -*- coding: utf-8 -*-
"""
Proje : Plaka tespit ve Erkan uyarı sistemi
@author: Selim INCE
"""

import sqlite3 #Database Module

dbconnect = sqlite3.connect('aracbilgi.db') #Database Connect Variable
database_select = dbconnect.cursor()  # Operation relation in Database

#Veritabanında tablo oluşturulması
database_select.execute('''
CREATE TABLE info
(id INTEGER PRIMARY KEY,
adsoyad VARCHAR(50),
telno INTEGER NOT NULL,
plaka VARCHAR(30))''')

#Add Data Database
database_select.execute('''INSERT INTO info(id,adsoyad,telno,plaka)
VALUES ('1','selim ince','5374276035','64 DR 984')''')

dbconnect.commit()
dbconnect.close()