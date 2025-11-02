# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 17:42:27 2025

@author: ACER
"""

drinks = ['kofe', 'choy', 'kokteyl', 'karak', 'toqa', 'aroq']
for drink in drinks:
    if drink == 'aroq':
        print(drink.upper(), "-Bu xarom")
    else:
        print(drink.title(),"-Tafaddol, hozir yetkazamiz!")
        
cars = ["toyota", "kia", "mercedes", "forza", "gm", "ravon"]
for car in cars:
    if car == "gm":
        print(car.upper())
    else:
        print(car)
        
        
cars = ["toyota", "kia", "mercedes", "forza", "gm", "ravon"]
for car in cars:
    if car != "gm":
        print(car)
    else:
        print(car.upper())
        
# javob = input("\n Ismingizni yozing!>>>")
# if javob.lower() == "admin":
#     print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yhatini ko'rishni hohlaysizmi?")
# else:
#     print("Hush kelibsiz,", javob.title())

# numbera,numberb = input("Salom, 2 ta raqam kiriting:>>>").split()
# numbera = int(numbera)
# numberb = int(numberb)

# if numbera == numberb:
#     print("Sonlar teng ekan!")
# else:
#     print("Yaxshi")

# son = int(input("Ixtiyoriy son kiriting, Musbat yoki manfiy ekanini aniqlab beraman InshaaAlloh!>>>"))
# if son >= 0:
#     print('Musbat son')
# else:
#     print('Manfiy son')
    
number = float(input("Ixtiyoriy son kiriting, men uni ildizini hisoblab beraman InshaAlloh, faqat musbat son bo'lsin!>>>"))
if number>0:
    print(number**(1/2))
else:
    print("Musbat son kiriting")
    