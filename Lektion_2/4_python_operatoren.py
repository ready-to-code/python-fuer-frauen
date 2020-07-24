# Potenzierung
print(4 ** 4)
print(pow(4, 4))

# Wurzel
print(4 ** 0.5)
print(pow(4, 0.5))

from cmath import sqrt

print(sqrt(4))

# Trigonometrische Funktionen und Konstanten
from math import sin, cos, tan
from math import e, pi
from math import pow

print(sin(90))
print(e)
print(pi)
print(pow(4,4))

# Verkürzte Schreibweise
wert = 100
wert = wert + 100
wert = wert * 10
print(wert)

wert = 100
wert += 100
wert *= 10
print(wert)

# Vergleichsausdrücke
print(2 > 7) # Ausgabe ist ein Boolean (= Zustandswert, TRUE oder FALSE)
print(2 < 7)
print(2 == 7)
print(5 == 5.0)
print(2 != 7)
print(2 <= 7)


# Logische Operatoren
print(not(5==5)) # not -> Gegenteil vom Boolean
print((2<7) and (5>4))
print((2<7) or (4>5))
