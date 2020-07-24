# Schleifen

from math import sqrt

#zahl = float(input("Bitte eine Zahl eingeben: "))
#wurzel = sqrt(zahl)
#print("Die Wurzel aus {0} ist {1}.".format(zahl, wurzel))

# if-Schleife

#zahl = float(input("Bitte eine Zahl eingeben: "))

#if zahl >= 0.0:
    #wurzel = sqrt(zahl)
    #print("Die Wurzel aus {0} ist {1}.".format(zahl, wurzel))
#if zahl < 0.0:
    #print("Aus einer negativen Zahl kann keine Quadratwurzel berechnet werden.")

# if-else-Schleife

#zahl = float(input("Bitte eine Zahl eingeben: "))

#if zahl >= 0.0:
    #wurzel = sqrt(zahl)
    #print("Die Wurzel aus {0} ist {1}.".format(zahl, wurzel))
#else:
    #print("Aus einer negativen Zahl kann keine Quadratwurzel berechnet werden.")

# elif-Schleife

currency = "€"

if currency == "$":
    print("US-Dollar")
else:
    if currency == "§":
        print("Britischer Pfund")
    else:
        if currency == "€":
            print("Euro")

####

currency = "€"

if currency == "$":
    print("US-Dollar")
elif currency == "§":
    print("Britischer Pfund")
else:
    print("Euro")

