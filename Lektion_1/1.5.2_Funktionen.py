from math import pi


def ausgabe(x, y):
    print("Die Flaeche ist %8.2f" % y)
    print("Der Umfang ist %8.2f" % x)
    print()


# Kreis
Radius = 10.0
Umfang = 2*pi*Radius
Flaeche = pi*Radius**2
ausgabe(Umfang, Flaeche)

# Rechteck
Hoehe = 10.0
Breite = 50.0
Umfang = 2*(Hoehe+Breite)
Flaeche = Breite*Hoehe
ausgabe(Umfang, Flaeche)