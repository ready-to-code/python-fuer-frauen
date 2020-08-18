# Tuples sind eine geordnete Zusammenfassung beliebiger Objekte
# Unterschied zu Arrays: Tuples sind unveraenderlich

werte = (10, 20 ,30) # Tuple
print(type(werte))

array = [10, 20, 30] # Array / Liste
print(type(array))

zahlen = 50, 45, 87, 10, 20, 30  # Tuple
print(type(zahlen))

print(werte == zahlen)
print(werte + zahlen)
print(werte)

print(3 * werte)

print(30 in werte)
print(60 in zahlen)

# Funktioniert nicht, da Tuple unveraenderlich sind
#werte.sort()
#print(werte)

# Moeglich, da sorted()-Funktion urspruengliches Array nicht veraendert
x = sorted(zahlen)
print(x)

for i in werte:
    print(i)

