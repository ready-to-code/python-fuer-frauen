from math import sqrt

a = float(input("Bitte trage die Laenge der Seite a in cm ein: "))
b = float(input("Bitte trage die Breite der Seite b in cm ein: "))

def satz_des_pythagoras(a, b):
    c = sqrt((a**2 + b**2))
    return c


hypothenuse = satz_des_pythagoras(a, b)

print("Die Seite c ist ", hypothenuse, " cm lang.")
# Die Bezeichnung von Funktionen folgt denselben Regeln wie für Variablen.



