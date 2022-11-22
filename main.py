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
        kiberelt_konyvek_kiirasa()

    elif bekert == "3":
        konyv_kiberlese()

    elif bekert == "4":
        pass
    
    elif bekert == "5":
        pass
    elif bekert == "6":
        pass