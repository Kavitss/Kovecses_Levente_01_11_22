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
    for key, value in kivett_konyvek.items():
        print(f"{key}\t\t{value}")

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

def mentes_kiberelt_konyvek():
    file = open(kivett_konyvek_filenev, "w", encoding="utf-8")
    for key, value in kivett_konyvek.items():
        file.write(f"{key};{value}\n")
    file.close()

def konyv_visszahozasa():
    system("cls")
    print("-------------------KÖNYV VISSZAHOZÁSA-------------------\n")
    kiberelt_konyvek_kiirasa()
    konyv = input("\nVisszahozott könyv neve: ")

    if konyv in kivett_konyvek:
        kivett_konyvek.pop(konyv)

        mentes_kiberelt_konyvek()
        input("Sikeres visszahozatal!\nTovább... ")
    else:
        print(f"A(z) {konyv} könyv nem szerepen a kivett könyvek listájában!")
        bekert_2 = input("0 - tovább\t\t1 - újrapróbálkozás\nVálasztás: ")
        if bekert_2 == "1":
            konyv_visszahozasa()

def mentes_osszes_konyv():
    file = open(osszes_kony_filenev, "w", encoding="utf-8")
    for i in range(len(osszes_konyv)):
        if i == 0:
            file.write(osszes_konyv[i])
        file.write(f"\n{osszes_konyv[i]}")

def osszes_konyvbol_torles():
    system("cls")
    print("-------------------KÖNYV TÖRLÉSE------------------\n")
    osszes_konyv_kiirasa()
    konyv_index = int(input("\nTörölni kívánt könyv: "))-1
    osszes_konyv.pop(konyv_index)
    mentes_osszes_konyv()
    input("Könyv törlése sikeres!\nTovább... ")
