from math import sqrt

a = float(input("Bitte trage die Länge der Seite a in cm ein: "))
b = float(input("Bitte trage die Länge der Seite b in cm ein: "))


# gleiche Regeln für den Namen wie bei Variablen
# Übergabeparameter: Eingabeparameter, welche die Funktion auszuwerten hat
def satz_des_pythagoras(a, b):
    c = sqrt((a**2+b**2))
    return c


hypotenuse = satz_des_pythagoras(a, b)

print("Die Seite c ist ", hypotenuse, " cm lang.")
print("Das Dreieck mit den Seitenlängen {0} cm und {1} cm ist in der Hypotenuse {2} cm lang".format(a, b, hypotenuse))
print("Das Dreieck mit den Seitenlängen {0:.2f} cm und {1:.2f} cm ist in der Hypotenuse {2:.2f} cm lang".format(a, b, hypotenuse))

