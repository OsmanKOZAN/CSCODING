# -*- coding: utf-8 -*-
#%% Sqlite
#kütüphaneyi import edelim
import sqlite3

con = sqlite3.connect("Kutuphane.db")

cur = con.cursor()

def tabloOlustur():
    cur.execute("Create Table if not exists Kitaplar(ID INTEGER PRIMARY KEY AUTOINCREMENT, AD text, YAZAR text, SAYFA int )")
    con.commit()

def veriEkle():
    cur.execute("insert into kitaplar values (1,'İstanbul Hatırası','Ahmet Ümit',561)")
    con.commit()    

def veriEkleKullanici():
    ad = input("Kitabın adını giriniz :")
    yazar = input("Kitabın yazarını giriniz :")
    sayfa = int(input("Kitabın sayfa sayını giriniz :"))
    
    cur.execute("insert into kitaplar values(?,?,?,?)",(None, ad, yazar, sayfa))
    con.commit()

def verileriAl():
    cur.execute("select * from Kitaplar")
    liste = cur.fetchall()
    #print(liste)
    print("Kitaplar Tablosu")
    for i in liste:
        print(i)
    
#    for i in cur:
#        print(i)

def verileriSadeceKitapYazarAdlariniAl():
    cur.execute("select AD, YAZAR from Kitaplar")
    liste = cur.fetchall()
    #print(liste)
    print("Kitap ve Yazarları Tablosu")
    for i in liste:
        print(i)

    
def kitapAra(kitapAd):
    cur.execute("Select * from Kitaplar Where AD = ?",(kitapAd,))
    liste = cur.fetchall()
    print(f"{kitapAd} aranan kitabın sonuçları")
    
    if len(liste)== 0:
        print("Aradığınız Kitap Bulunamadı")
    else:
        for i in liste:
            print(i)
    
def veriGuncelle(eskiKitapAd, yeniKitapAd):
    cur.execute("update Kitaplar Set AD=? where AD=?",(yeniKitapAd,eskiKitapAd))
    con.commit()
    
def veriSil(silinecekID):
    cur.execute("delete from Kitaplar where ID = ? ",(silinecekID,))
    con.commit()
    
#Create Table
tabloOlustur()
#veriEkle()
#veriEkleKullanici()

verileriAl()
verileriSadeceKitapYazarAdlariniAl()

kitapAra("Kainatın Şifresi")

veriGuncelle("Kainatın Şifresi", "Dünyanın Şifresi")

veriSil(1)

verileriAl()
con.close()
#%%
