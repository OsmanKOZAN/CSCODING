
# -*- coding: utf-8 -*-
#%% Sqlite
#kütüphaneyi import edelim
import sqlite3

con = sqlite3.connect("Kutuphane.db")

cur = con.cursor()

def tabloOlustur():
    cur.execute("Create Table if not exists Kitaplar(ID int, AD text, YAZAR text, SAYFA int )")
    con.commit()

#Create Table
tabloOlustur()

con.close()
