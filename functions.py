from data import osszes_konyv, kivett_konyvek, kiberelt_konyvek_nevei
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
    print("7 - elérhető könyvek kiirása")

def data_megtoltes():

    #összes könyvek
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
    print("-------------------KÖNV KIBÉRLÉSE-------------------\n")
    elerheto_konyvek_kiirasa()
    konyv = input("\nKönyv neve: ")
    if (konyv in kiberelt_konyvek_nevei) != True and (konyv in osszes_konyv) == True:                                                    #nincsen benne a kivett könyvekbe, viszont benne vanaz összes könyvekben 
        berlo = input("Kibérlő neve: ")
        kivett_konyvek[konyv] = berlo
        mentes_utolso_helyre_kiberelt_konyvek(konyv,berlo)
        input("\nSikeres felvétel!\nTovább... ")
    else:
        bekert_2 = input("\nNincs ilyen nevű könyv!\n0 - Tovább \t\t 1 - Újra \t\t 2 - Könyv hozzáadása az összes könyvekhez\nVálasztott: ")
        if bekert_2 == "1":
            konyv_kiberlese()
        elif bekert_2 == "2":
            uj_konyv_felvetele()
        
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
        input("\nSikeres visszahozatal!\nTovább... ")
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
    file.close()

def osszes_konyvbol_torles():
    system("cls")
    print("-------------------KÖNYV TÖRLÉSE------------------\n")

    osszes_konyv_kiirasa()
    konyv_index = input("\nTörölni kívánt könyv sorszáma: ")
    try:
        konyv_index = int(konyv_index)-1                                                                            #számmá próbálja konvertálni

    except ValueError:
        bekert_2 = input("\nKérem számot adjon meg!\n0 - tovább \t\t 1 - Újra\nVálasztás: ")                          #ha nem sikerül: problémázik
        if bekert_2 == "1":
            osszes_konyvbol_torles()

    else:                                                                                                           #ha sikerül: 
        try:                                                                                                                #megpróbálja kitörölni a listából                                                                                     
            osszes_konyv.pop(konyv_index)

        except IndexError:                                                                                                  #ha nem sikerül: problémázik
            bekert_2 = input("\nNincs ilyen sorszámú könyv!\n0 - tovább \t\t 1 - Újra\nVálasztás: ")
            if bekert_2 == "1":
                osszes_konyvbol_torles()
                
        else:                                                                                                               #ha sikerül: minden hapy
            mentes_osszes_konyv()   
            input("\nKönyv törlése sikeres!\nTovább... ")

def mentes_utolso_helyre_osszes_konyv(konyv):
    file = open(osszes_kony_filenev, "a", encoding="utf-8")
    file.write(f"\n{konyv}")
    file.close()

def uj_konyv_felvetele():
    system("cls")
    print("-------------------ÚJ KÖNYV FELVÉTELE------------------\n")
    uj_konyv = input("Könyv neve:")
    osszes_konyv.append(uj_konyv)
    mentes_utolso_helyre_osszes_konyv(uj_konyv)
    input("\nKönyv felvétele sikeres!\nTovább... ")

def elerheto_konyvek_kiirasa():
    for i in kivett_konyvek:
        kiberelt_konyvek_nevei.append(i)

    for i in osszes_konyv:
        if (i in kiberelt_konyvek_nevei) != True:
            print(i)