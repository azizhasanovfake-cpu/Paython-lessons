# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 14:50:31 2025

@author: ACER
"""

twin = list(range(0, 67, 2))
print(twin)
uzunligi = len(twin)
print(uzunligi)
print(max(twin))
print(min(twin))
print(sum(twin))
languages = ['python', 'Java Script', 'C++', 'C#', 'Node']
#ayrimlari = languages[1:3]
phones = ['REDMI', 'IPHONE', 'HONOR', 'LG']
my_phones = tuple(phones)
# qayt = list(my_phones)
# print(qayt)
#for language in languages:
#print('Eng yaxshi til bu ', language)
print(languages)
for lang in languages:
    print("Eng yaxshi til bu ", lang)
    print(f"Salom {lang}, Sen eng yaxshisisan")
    
sonlar = list(range(1,11))
print(sonlar)
sonlar_kv = []
for son in sonlar:
    sonlar_kv.append(son**2)
print(sonlar_kv) 
#dostlar = []
#for n in range(5):
#    dostlar.append(input(f"{n+1} do'stingizni ismini kiriting:"))
#print(dostlar)

numbers = []
results = []
birinchi = []
#for r in sonlar:
    #birinchi.append(input("ixtiyoriy son kiriting: "))
    #print("Siz kiritgan son " birinchi)
    
days = []
for d in range(7):
    days.append(input(f"{d+1} hafta kuni qaysi? Yozing: "))
    print(days[-1])
print("Hafta kunlari shundaymi? ", days)


