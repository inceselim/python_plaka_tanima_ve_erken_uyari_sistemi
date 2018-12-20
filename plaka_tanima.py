# -*- coding: utf-8 -*-
"""
Proje : Plaka tespit ve Erkan uyarı sistemi
@author: Selim INCE
"""

import pytesseract
from PIL import Image

print ("Tarama baslatildi ...")
plakakarakter1 = (pytesseract.image_to_string(Image.open('plaka0.jpg')))

if (plakakarakter1):
    print "Tespit Edilen plaka : ", plakakarakter1
else:
    print ("Plaka Karakter Tespiti Başarısız Oldu...")
    

plakakarakter2 = (pytesseract.image_to_string(Image.open('plaka1.jpg')))