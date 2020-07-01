# Strings - Zeichenketten
Erster_Name = "DHBW "
Zweiter_Name = 'Stuttgart'
Name = Erster_Name + Zweiter_Name

print(Name)
print(len(Zweiter_Name))

# darf nicht mit einer Ziffer beginnen
# Underscore ist jedoch als erstes Zeichen erlaubt
# Variable darf auch nur aus Underscores bestehen

import keyword
print(keyword.kwlist)

# Schreibweisen von Variablen
letzterGespeicherterWert = 123 # Camel Case
LetzterGespeicherterWert = 123 # Pascal Case
letzter_gespeicherter_wert = 123 # Snake Case

alter = 20

print("Ich bin: " + str(alter))
# print("Ich bin: " + age)  --> Dies würde eine Fehlermeldung geben.

Stuggi = 5 * Zweiter_Name

print(Stuggi)

anzahl_strich = 8
strich = anzahl_strich * "-"

print(strich)

# =-Zeichen ist dabei nicht mit dem mathematischen Istgleich-Zeichen zu verwechseln; es stellt eine Zuweisung der rechten Seite zur linken Seite dar
# erst wird die Operation auf der rechten Seite ausgeführt und dann der linken Seite zugewiesen
# Variable muss auf der linken Seite stehen

# 102 = startwert # Fehler!
# Stadt + startwert = Ergebnis # Fehler!

# Variablentypen

# Integer - Ganze Zahlen
type(3)

x = int(42)
print(x)

y = int(42.3)
print(y)

# int(42 Grad) # Fehlermeldung

print(strich)

# Float - Gleitpunktzahlen
# Mehrere Wege zur Darstellung der Zahl 3000,0
x1 = 3000.0
x2 = 3e+3
x3 = 3.0e3
x4 = 3E3
x5 = 3.e+3
print(x1,x2,x3,x4,x5)

print(strich)

# Complex - Komplexe Zahlen
# bestehend aus einem Realteil a und einem Imaginärteil b, j ist die Imaginäre Einheit bei der j = (-1)^1/2 gilt
z1 = 3.0 - 5.0j
z2 = complex(3.0,-5.0)
z3 = 3 - 5j
print(z1, z2, z3)

# kein Leerzeichen zwischen b und j
# kein *-Zeichen zwischen b und j

print(strich)

# Binärzahlen
x = 0b101010
print(x)

y = bin(42)
print(y)

print(strich)

# Dynamisch typisiert
Name = "Müller"
Vorname = "Sabine"
Alter = 20
Studiengang = "Wirtschaftsingenieurwesen"
Semester = 1

print("Name, Vorname:", Name, Vorname, " Alter:", Alter)
print("Studiengang:", Studiengang, " Semester:", Semester)

Name = 'Mueller'
Vorname = 'Sabine'
Alter = 20.4
Studiengang = 'Irgend etwas mit Wirtschaft'
Semester = 'Erstes'

print(strich)

print("Name, Vorname:", Name, Vorname, " Alter:", Alter)
print("Studiengang:", Studiengang, " Semester:", Semester)

# Python ermittelt in der Laufzeit von welchem Typ die Variable ist
# In statisch typisierten Sprachen muss dagegen jeder Variablen auch ein Typ zugewiesen werden, der sich danach nicht mehr ändern lässt.

print(strich)

# Python arbeitet das Programm so wie man es liest, von oben nach unten (sequenzielle Programmabarbeitung)
variable1 = 32
variable2 = variable1

variable1 = 64
print("Variable 1:", variable1)
print("Variable 2:", variable2)

# deklarationsfreie Sprache
# Variablen können unterschiedliche Typen an sich binden

startwert = 102
print(startwert)
startwert = 1043.56
print(startwert)
startwert = "Wuppertal"
print(startwert)

print(strich)

# Konstanten definieren
MAXIMALE_FEHLERVERSUCHE = 3  # Sollte konstant gehalten werden

print(strich)

# Rechnen mit Variablen
# Konvertierung in andere Typen
# Umrechnung von Grad Celsius in Grad Fahrenheit
print("Umrechnung der Temperaturen von Celsius in Fahrenheit")
Celsius = input("Bitte geben Sie eine Temperatur in Celsius ein: ")
Celsius = float(Celsius)
Fahrenheit = 9/5 * Celsius + 32 # wird von links nach rechts ausgeführt; rechte Seite wird ausgeführt und der linken Seite (Variable) zugeordnet -> nicht dasselbe wie das mathematische Gleichheitszeichen
print("Sie haben {0} Grad Celsius eingegeben.".format(Celsius)) # %f dient als Platzhalter für die anstehende Variablenzuweisung (Dezimalzahlen)
print("Diese Temperatur entspricht {0} Grad Fahrenheit.".format(Fahrenheit))
