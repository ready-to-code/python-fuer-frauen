# auch Mengen
# ungeordnete Zusammenfassung von Objekten, wobei jedes Element nur einmal darin vorkommen kann
# Listen können keine Elemente von Sets sein

Menge_1 = set([12, 34, 60, 12, 72, 34, 90])
Menge_2 = set([17, 90, 34, 34, 112, 9, 12])

print(Menge_1)
print(Menge_2)

# Durchschnitt bzw. Schnittmenge
print(Menge_1 & Menge_2)

# Differenz
print(Menge_1 - Menge_2)
print(Menge_2 - Menge_1)

# Vereinigung
print(Menge_1 | Menge_2)

for i in Menge_1:
    print(i)

