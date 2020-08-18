# ungeordnete Zusammenfassung von Schluessel-Wert-Paaren bzw. assoziative Arrays
# aehnlich wie eine Tabelle aufgebaut / JSON-Format aehnlich
# jedem Datenwert (data value) wird ein Schluesselwert (key value) zugeordnet
# die Datenwerte durfen aus Listen bestehen, die Schluesselwerte jedoch nicht

woerterbuch = {"Projekt Management":"Project Management", "gelb":"yellow", "gruen":"green"}
kfz = {"DO":"Dortmund", "HB":"Bremen", "E":"Essen", "W":"Wuppertal"}
print(kfz["DO"]) 
# print(kfz["Bremen"])  -> Bremen ist kein key value, sondern data value

print(type(woerterbuch))
print(woerterbuch)

# Hinzufuegen von weiteren key-value-Paaren
kfz["B"] = "Berlin"
print(kfz)

neu = {}
print(type(neu))
print(neu)

print("erste Zeile \nnaechste Zeile")

n = "erste Zeile \nnaechste Zeile"
print(n) # = print("erste Zeile \nnaechste Zeile")

