from functions import *
from os import system
bekert = ""

#adatok betöltése
data_megtoltes()

while bekert != "0":
    menu()
    bekert = input("\nVálasztott: ")

    if bekert == "1":
        system("cls")
        print("-------------------ÖSSZES KÖNYV-------------------\n")
        osszes_konyv_kiirasa()
        input("\nTovább...  ")

    elif bekert == "2":
        system("cls")
        print("-------------------KIBÉRELT KÖNYVEK-------------------\n")

        kiberelt_konyvek_kiirasa()

        input("\nTovább... ")

    elif bekert == "3":
        konyv_kiberlese()

    elif bekert == "4":
        konyv_visszahozasa()
    
    elif bekert == "5":
        osszes_konyvbol_torles()

    elif bekert == "6":
        uj_konyv_felvetele()

    elif bekert == "7":
        system("cls")
        print("-------------------ELÉRHETŐ KÖNYVEK------------------\n")

        elerheto_konyvek_kiirasa()
        
        input("\nTovább... ")