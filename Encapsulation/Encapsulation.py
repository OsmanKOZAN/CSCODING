# -*- coding: utf-8 -*-
#%% Encapsulation
class BankaHesap():
    def __init__(self, adSoyad, bakiye, adres):
        self.adSoyad = adSoyad
        self.__bakiye = bakiye
        self.adres = adres
    # get ve set metodu
    def getMoney(self):
        return self.__bakiye
    
    def setMoney(self, miktar):
        self.__bakiye = miktar
        return self.__bakiye
    
    #private
    def __zamYap(self, oran):
        self.__bakiye = (self.__bakiye) + ((self.__bakiye * oran) / 100 )
        return self.__bakiye
        

mus1 = BankaHesap("Osman KOZAN", 5000, "İzmir")
mus2 = BankaHesap("Hakime KOZAN", 10000, "Seferihisar")

print(mus1.getMoney())
print(mus1.setMoney(250000))

