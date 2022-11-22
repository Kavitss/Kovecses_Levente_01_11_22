from functions import *
from os import system
bekert = ""

#adatok betöltése
data_megtoltes()

while bekert != "0":
    menu()
    bekert = input("Választott: ")

    if bekert == "1":
        system("cls")
        print("-------------------ÖSSZES KÖNYV-------------------")
        osszes_konyv_kiirasa()
        input("\nTovább...  ")

    elif bekert == "2":
        system("cls")
        print("-------------------KIBÉRELT KÖNYVEK-------------------")

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