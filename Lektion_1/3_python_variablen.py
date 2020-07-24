# Strings - Zeichenketten
Erster_Name = "PyLadies"
Zweiter_Name = "Stuttgart"

# Fehler:
# "PyLadies" = Erster_Name
# 1ster_Name = "PyLadies"
# Erster Name = "PyLadies"

Name = Erster_Name + " " + Zweiter_Name

print(Name)
print(len(Zweiter_Name))

# Variablenbezeichnung:
# - darf nicht mit einer Zahl beginnen
# - Underscore ist erlaubt (auch nur aus Underscore bestehen)
# - Variable muss auf der linken Seite vom = stehen
# - darf nur aus einer Zeichenkette bestehen

_____ = "Tin Votan"
print(_____)
print(len(_____))

# Schreibweisen von Variablen
letzterGespeicherterWert = 123 # Camel Case
LetzterGespeicherterWert = 123 # Pascal Case
letzter_gespeicherter_wert = 123 # Snake Case

tuerkei = 'Türkei'
print(tuerkei)

alter = 20
print("Ich bin: " + str(alter)) # Kombination von Argumenten
print("Ich bin: ", alter) # Auflistung von Argumenten

jahre = 5 + alter
print(jahre)

# Abruf eines Strings 
Stuggi = 5 * Zweiter_Name
print(Stuggi)

# Funktioniert nicht, da Kombination zwischen Integer und String sinnlos ist
# Stuttgart = 5 + Zweiter_Name
# print(Stuttgart)

# Integer - Ganze Zahlen
print(type("drei"))
print(type(3))

x = int(42)
print(x)

y = int(42.7)
print(y)

# Fehler
# z = int(42 "Zweiundvierzig")
# print(z)

b = round(42.7)
print(b)

# Float - Gleitpunktzahlen / Dezimalzahlen

x1 = 3000.0
x2 = 3e+3
x3 = 3.0e3
x4 = 3E3
x5 = 3.e+3

print(x1, x2, x3, x4, x5)

y3 = 2.34e3
print(y3)

# Complex - Komplexe zahlen
# bestehend aus einem Realteil a und einem Imaginärteil b; j ist die Imaginäre Einheit
z1 = 3.0 - 5.0j
z2 = complex(3.0, -5.0)
z3 = 3 - 5j

print(z1, z2, z3)

# Boolean - Zustandswerte (binäre)
x = True
y = False

# Fehler
# True = "Weihnachtsmann"
# print(True)

# Binärzahlen
x = 0b101010
print(x)

y = bin(42)
print(y)

# Dynamisch typisiert
Name = "Müller"
Vorname = "Sabine"
Alter = 20
Studiengang = "Maschinenbau"
Semester = 1

print("Name, Vorname: ", Name, Vorname, "Alter: ", Alter)
print("Studiengang: ", Studiengang, "Semester: ", Semester)

Name = "Mueller"
Vorname = 'Sabine'
Alter = 20.4
Studiengang = "Irgend etwas Technisches"
Semester = 'Erstes'

print("Name, Vorname: ", Name, Vorname, "Alter: ", Alter)
print("Studiengang: ", Studiengang, "Semester: ", Semester)

# Hinweis auf sequenzielle Syntax / von oben nach unten laufend
variable1 = 32
variable2 = variable1

variable1 = 64
print("Variabel 1: ", variable1)
print("Variabel 2: ", variable2)

# Konstanten definieren
ZAHL_PI = 3.1415692475
print(ZAHL_PI)

# Konvention für andere Python-Programmierer
ZAHL_PI = "Kartoffelsalat"
print(ZAHL_PI)

# Groß- und Kleinschreibung ist relevant
print(ZAHL_PI)
#Print(ZAHL_PI)

MAXIMALE_FEHLVERSUCHE = 3

# Rechnen mit Variablen
# Konvertierung in andere Typen
# Umrechnung von Grad Celsius in Grad Fahrenheit
print("Umrechnung der Temperaturen von Celsius in Fahrenheit")
Celsius = input("Bitte geben Sie eine Temperatur in Celsius ein: ")
Celsius = float(Celsius)
Fahrenheit = 9/5 * Celsius + 32
print("Sie haben {0} Grad Celsius eingegeben.".format(Celsius)) # {0} -> Platzhalter
print("Diese Temperatur entspricht {0} Grad Fahrenheit.".format(Fahrenheit))
print("Die Celsius-Temperatur {0} entspricht in Grad Fahrenheit {1}.".format(Celsius, Fahrenheit))