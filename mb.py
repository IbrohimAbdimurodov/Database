import sqlite3

boglanish = sqlite3.connect("mydatabase.db")

malumot = boglanish.cursor()

malumot.execute('''
CREATE TABLE IF NOT EXISTS Kompyuterlar(
    nomi TEXT
    narxi TEXT
    xotirasi TEXT)

'''
)

malumot.execute('''
CREATE TABLE IF NOT EXISTS Odamlar(
    ismi TEXT
    familiyasi TEXT
    yoshi TEXT)

'''

)

malumot.execute(''' 
CREATE TABLE IF NOT EXISTS Hayvonlar(
    turi TEXT
    rangi TEXT
    oziqlanishi TEXT)

'''

)
malumot.execute('''
CREATE TABLE IF NOT EXISTS Mashinalar(
    narxi TEXT
    yili TEXT
    malumotlari TEXT)

'''
)