from math import sqrt

zahl = float(input("Bitte eine Zahl eingeben: "))
wurzel = sqrt(zahl)
print("Die Wurzel aus {0} ist {1} ".format(zahl, wurzel))

# Lösung für das Problem mit if:
# geschachtelte Anweisungen

zahl = float(input("Bitte eine Zahl eingeben: "))
if zahl >= 0.0:
    wurzel = sqrt(zahl)
    print("Die Wurzel aus {0} ist {1} ".format(zahl, wurzel))
if zahl < 0.0:
    print("Aus einer negativen Zahl kann keine Quadratwurzel berechnet werden. Geben Sie eine positive Zahl ein!")

# else

zahl = float(input("Bitte eine Zahl eingeben: "))
if zahl >= 0.0:
    wurzel = sqrt(zahl)
    print("Die Wurzel aus {0} ist {1}".format(zahl, wurzel))
else:
    print("Aus einer negativen Zahl kann keine Quadratwurzel berechnet werden. Geben Sie eine positive Zahl ein!")

# elif

currency = "€"

if currency == "$":
    print("US-Dollar")
else:
    if currency == "¥":
        print("Japanischer Yen")
    else:
        if currency == "€":
            print("Euro")

# Lösung

currency = "£"

if currency == "$":
    print("US-Dollar")
elif currency == "¥":
    print("Japanischer Yen")
elif currency == "€":
    print("Euro")
else:
    print("Sonst")

