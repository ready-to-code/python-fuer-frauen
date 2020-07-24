# Berechnung von Umfang und Flaeche eines Kreises mithilfe von Funktionen

w = "global" # globale Variable

from math import pi

def ausgabe(x, y):
    print("Die Flaeche ist %8.4f" % y) # % -> Platzhalter innerhalb von Funktionen / 8 -> Anzahl der anzuzeigenen Zeichen
    print("Der Umfang ist %8.4f" % x)
    print()

    print(w)

    r = "lokal" # lokale Variable

# Kreis
radius = 10.0
umfang_kreis = 2 * pi * radius
flaeche_kreis = pi * radius ** 2
ausgabe(umfang_kreis, flaeche_kreis)

# Rechteck
hoehe = 10.0
breite = 50.0
umfang_rechteck = 2 * (hoehe + breite)
flaeche_rechteck = breite * hoehe
ausgabe(umfang_rechteck, flaeche_rechteck)

# Fehlermeldung, weil lokale Variable
# print(r)
