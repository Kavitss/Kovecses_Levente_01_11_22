from data import osszes_konyv, kivett_konyvek
from os import system

osszes_kony_filenev = "ossz_konyv.txt"
kivett_konyvek_filenev = "kivett_konyvek.txt"

def menu():
    system("cls")
    print("-------------------MENÜ-------------------")
    print("0 - kilépés")
    print("1 - összes könyv kiírása")
    print("2 - kibérelt könyvek kiírása")
    print("3 - könyv kibérlése")
    print("4 - könyv visszahozása")
    print("5 - összes könyvből törlés")
    print("6 - új könyv feljegyzése")


def data_megtoltes():
    #osszes elérhető könyvek
    file = open(osszes_kony_filenev,"r",encoding="utf-8")
    for row in file:
        osszes_konyv.append(row.strip())
    
    file.close()
    #kivett könyvek 
    file = open(kivett_konyvek_filenev, "r", encoding="utf-8")
    for row in file:
        szeletelt = row.strip().split(";")
        kivett_konyvek[szeletelt[0]] = szeletelt[1]
    file.close()