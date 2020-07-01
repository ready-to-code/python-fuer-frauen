# Einfache Rechenoperationen

print("Hello World!")

# Addition und Subtraktion
# 1 + 2 # würde nur im Hintergrund des Python-Interpreters laufen
print(1 + 2)
print(1 - 2)

# Multiplikation und Division
print(1 * 2)
print(1 / 2)

# Potenzierung
print(4 ** 4)
print(pow(4, 1/2))

# Wurzel
print(4 ** 0.5)

from cmath import sqrt

print(sqrt(4))

# Ganzzahlige Division und Modulo-Operator
print(7 // 3)
print(7 % 3)

# Trigonometrische Funktionen

from math import sin, cos, tan
from math import e, pi
from math import pow

print(sin(90))
print(e)
print(pi)

# Rechenregeln
r1 = (1 + 2) * 3
print(r1)
r2 = 1 + 2 * 3
print(r2)

# Verkürzte Schreibweise
wert = 100
wert = wert + 100
wert = wert*10

print(wert)

## Äquivalent zu:

wert = 100
wert += 100
wert *= 10

print(wert)

# Vergleichsausdrücke
# Ausgabe ist ein boolean
print(2 > 7)
print(2 < 7)
print(2 == 7)
print(5 == 5)
print(2 != 7)
print(5 <= 5)

# Logische Ausdrücke
print(not(5==5))  # print(not(5!=5))
print((2 < 7) and (5 > 4))
print((2 > 7) or (4 > 5))
