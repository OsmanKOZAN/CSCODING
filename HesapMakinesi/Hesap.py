# -*- coding: utf-8 -*-
#%% calc
class calc(object):
    "Hesap Makinesi"
    #init metodu
    def __init__(self, a, b):
        #attribute
        self.value1 = a
        self.value2 = b
        
    def add(self):
        "Toplama İşlemi"
        return self.value1 + self.value2
    
    def multiply (self):
        "Çarpma işlemi"
        return self.value1 * self.value2

try:
    v1 = int(input("Birinci sayıyı giriniz : "))
    v2 = int(input("Birinci sayıyı giriniz : "))
    secim = int(input("Yapılacak işlemi seçiniz :\n1. Toplama\n2.Çarpma :"))
    c1 = calc(v1,v2)
    if secim == 1 :
        addResult = c1.add()
        print(f"Toplama : {addResult}")
    elif secim == 2 :
        multiplyResult = c1.multiply()
        print(f"Çarpma : {multiplyResult}")
    else:
        print("Geçersiz İşlem")
except ValueError:
    print("Lütfen tam sayı giriniz.")



#%%

