# Berechnung von Flaeche und Umfang
from math import pi

# Kreis
Radius = 10.0
Umfang = 2*pi*Radius
Flaeche = pi*Radius**2
print("Die Flaeche ist %8.2f" % Flaeche)
print("Der Umfang ist %8.2f" % Umfang)
print()

# Rechteck
Hoehe = 10.0
Breite = 50.0
Umfang = 2*(Hoehe+Breite)
Flaeche = Breite*Hoehe
print("Die Flaeche ist %8.2f" % Flaeche)
print("Der Umfang ist %8.2f" % Umfang)
print()