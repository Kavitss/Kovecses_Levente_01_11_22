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

def osszes_konyv_kiirasa():
    for i in range(len(osszes_konyv)):
        print(f"{i+1}\t{osszes_konyv[i]}")
    
def kiberelt_konyvek_kiirasa():
    system("cls")
    print("-------------------KIBÉRELT KÖNYVEK-------------------")

    for key, value in kivett_konyvek.items():
        print(f"{key}\t\t{value}")
    
    input("\nTovább... ")

def mentes_utolso_helyre_kiberelt_konyvek(konyv, nev):
    file = open(kivett_konyvek_filenev, "a", encoding="utf-8")
    file.write(f"\n{konyv};{nev}")
    file.close()

def konyv_kiberlese():
    system("cls")
    print("-------------------KÖNV KIBÉRLÉSE-------------------")
    osszes_konyv_kiirasa()
    konyv_index = int(input("Könyv sorszáma: "))
    berlo = input("Kibérlő neve: ")
    kivett_konyvek[osszes_konyv[konyv_index -1]] = berlo
    mentes_utolso_helyre_kiberelt_konyvek(osszes_konyv[konyv_index -1],berlo)
    input("Sikeres felvétel!\nTovább... ")