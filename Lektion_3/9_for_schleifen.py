# i entspricht der Schleifenvariable
# einfache Schleife mit dem Quadrat der Zahl von 1 bis 4
for i in 1, 2, 3, 4:
    print(i, i*i)

# Zählen von 1 bis 9
# range(startwert(inklusiv), endwert(exklusiv), schrittweite)
for n in range(1, 10, 1):
    print(n)


# Laufvariablen für range() definieren
start = int(input("Startwert des Zählers: "))
ende = int(input("Endwert des Zählers: "))
schrittweite = int(input("Schrittweite des Zählers: "))

for i in range(start, ende, schrittweite):
    print(i)


# Rückwärts zählen
for i in range(10, 0, -1):
    print(i)
