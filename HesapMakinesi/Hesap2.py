# -*- coding: utf-8 -*-
#%% Hesap Makinesi
class HesapMakinesi(object):
    "Hesap Makinesi Classı"
    def __init__(self, a, b):
        "Varsayılan değerler"
        self.value1 =  a
        self.value2 = b
    
    def ToplamaIslemi(self):
        "Toplama işlemi a + b = sonuc "
        return self.value1 + self.value2
    
    def CarpmaIslemi(self):
        "Çarpma İşlemi a *b = sonuc"
        return self.value1 * self.value2
    
    def BolmeIslemi(self):
        if self.value1 == 0 or self.value2 == 0:
            print("Hiçbir Sayı 0 bölünmez")
        else:
            return self.value1 / self.value2
    
    def CikarmaIslemi(self):
        return self.value1 - self.value2

v1 = int(input("Birinci Sayısı Giriniz :"))
v2 = int(input("İkinci Sayısı Giriniz :"))

islem = int(input("1. Toplama\n2. Çarpma\n3. Bölme\n4. Çıkarma\nSeçim :"))
hm1 = HesapMakinesi(v1, v2)
if islem == 1 :
    toplamaSonuc = hm1.ToplamaIslemi()
    print(f"Toplama Sonucu {toplamaSonuc} olarak hesaplanmıştır. ")
elif islem == 2:
    carpmaSonuc = hm1.CarpmaIslemi()
    print(f"Çarpma Sonucu {carpmaSonuc} olarak hesaplanmıştır. ")
elif islem == 3:
    bolmeSonuc = hm1.BolmeIslemi()
    print(f"Bölme Sonucu {bolmeSonuc} olarak hesaplanmıştır. ")
elif islem == 4:
    cikarmaSonuc = hm1.CikarmaIslemi()
    print(f"Çıkarma Sonucu {cikarmaSonuc} olarak hesaplanmıştır. ")
else:
    print("Geçersiz Seçim")
#%%

