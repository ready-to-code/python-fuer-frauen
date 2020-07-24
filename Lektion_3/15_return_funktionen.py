# Parameterrueckgabe und Rueckgabewerte bei Funktionen

def fakultaet(n): # n ist der Parameter
    p = 1
    for i in range(n):
        p = p * (i+1)
    return p

print(fakultaet(7)) # 7 ist Argument
print(fakultaet(42))

# Mehrere Parameter
def volumen_wuerfel(laenge, breite, hoehe):
    volumen = laenge * breite * hoehe
    return volumen

print(volumen_wuerfel(8, 5, 3))
