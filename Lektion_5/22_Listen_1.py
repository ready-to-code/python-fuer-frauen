# eine Liste ist eine geordnete Zusammenfassung von Elementen
# auch als Array bekannt

a = [11, 3, 5, 7, 9]

print(a)
print(a)

# unterschiedliche Datentypen bzw. beliebige Objekte
b = [2, "Hallo", 12.5]
print(b)

# auch eine Liste / Array ist ein Objekt und kann daher gespeichert werden
c = [[2, 4], ['a', 'b']]
print(c)

# definierte Variablen können ebenfalls gespeichert werden
d = [a, b, c]
print(d)

# Zugriff auf bestimmtes Element eines Arrays
print(a[0], a[3])

print(c[1][1])

print(c[0][1])

# Listen-Operatoren
# Listen sind iterierbare Objekte , daher können Funktionen und Operatoren eingesetzt werden

# in-Funktion
moegliche_farben = [
    "rot", 
    "gruen", 
    "blau"
    ]

#farbe = input("Bitte Farbe eingeben: ")

#if farbe in moegliche_farben:
#    print("Diese Farbe ist enthalten!")
#else:
#    print("Diese Farbe ist nicht enthalten!")

# len-Funktion
anzahl = len(moegliche_farben)

for i in range(0, anzahl, 1):
    print(i, moegliche_farben[i])

# Wiederholung:
print(moegliche_farben[1])

for i in range(0, 10, 2):
    print(i)

# range(0, 10, 1) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# aequivalent zu:
for i in moegliche_farben:
    print(i)

# aequivalent zu:
for i in moegliche_farben:
    j = moegliche_farben.index(i)
    print(j, i)

# Sortieren (aufsteigend)
inhalt = [5.5, 23, 45, 15.3, 22, 54]
print(inhalt)

# urspruengliches Array wird nicht veraendert
x = sorted(inhalt)
print(x)
print(inhalt)

# urspruengliches Array wird veraendert
inhalt.sort()
print(inhalt)

# Sortieren (absteigend) -> Absteigend sortieren durch Kombination von sort() und reverse()
inhalt.reverse()
print(inhalt)

inhalt = [23.5, 12, [19, "Hallo"], 12, 45]
print(inhalt)

# Anhaengen von neuen Elementen
inhalt.append(100)
print(inhalt)

inhalt.extend((100, 200, 300)) # -> Tuple für (100, 200, 300)
print(inhalt)

inhalt.extend([100, 200, 300]) # -> Array für (100, 200, 300)
print(inhalt)

print(inhalt)
print(type(inhalt).__name__)

# Zaehlen
anzahl = inhalt.count(100)
print(anzahl)

# Loeschen
inhalt.remove(23.5)
print(inhalt)

# Index fragen
index = inhalt.index(45)
print(index)

# Einfuegen an spezifischer Stelle
inhalt.insert(3, 77) # 3 -> Index ; 77 -> hinzuzufuegendes Element
print(inhalt)

inhalt = [5.5, 23, 45, 15.3, 22, 54]

inhalt.sort(reverse=True)
print(inhalt)
