from functions import *

bekert = -1

#adatok megtöltése
data_megtoltes()

while bekert != 0:
    menu()
    bekert = int(input("Választott: "))

    if bekert == 1:
        osszes_konyv_kiirasa()
    elif bekert == 2:
        kiberelt_konyvek_kiirasa()
    elif bekert == 3:
        pass
    elif bekert == 4:
        pass
    elif bekert == 5:
        pass
    elif bekert == 6:
        pass