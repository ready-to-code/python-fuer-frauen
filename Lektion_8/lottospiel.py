strich = 30 * "-"

print("+++ Lottospiel mit variabler Anzahl an Auswahlmoeglichkeiten und Ziehungen")

# Berechnung der Fakultaet
def fakultaet(x): # x -> Parameter
    p = 1

    for i in range(x):    # 6! = 1 x 2 x 3 x 4 x 5 x 6  => [1, 2, 3, 4, 5] -> range(x) => iterierbares Pbjekt
        p = p * (i + 1)

    return p


# Berechnung Kombination (ohne W)
def zahlenlotto_ohne_wiederholung(n, k):
    h = fakultaet(n)
    j = fakultaet(n - k) * fakultaet(k)
    y = int(h / j)

    print("Es existieren {0} verschiedene Kombinationsmoeglichkeiten fuer das Lottospiel ohne Wiederholung der Zahlen, wenn man aus insgesamt {1} Zahlen davon {2} Zahlen aussuchen darf.".format(y, n, k))    


# Berechnung Kombination (mit W)
def zahlenlotto_mit_wiederholung(n, k):
    m = (n + k - 1)
    h = fakultaet(m)
    j = fakultaet(m - k) * fakultaet(k)
    y = int(h / j)

    print("Es existieren {0} verschiedene Kombinationsmoeglichkeiten fuer das Lottospiel mit Wiederholung der Zahlen, wenn man aus insgesamt {1} Zahlen davon {2} Zahlen aussuchen darf.".format(y, n, k))


# Menue abfragen
def menue():
    print(strich)
    print("Menue: ")
    print("(1) Neue Auswahl")
    print("(2) Beenden")
    print(strich)

    # gewuenschte Menueabfrage
    auswahl = int(input("Deine Auswahl: "))

    return auswahl


# Hauptprogramm
def main():
    while True:

        auswahl = menue()

        if auswahl == 1:
            n = int(input("Bitte gib die Menge der Auswahlmoeglichkeiten an: "))
            k = int(input("Bitte gib die Menge der Ziehungen an: "))

            if n >= k:
                print(strich)
                zahlenlotto_ohne_wiederholung(n, k)

                print(strich)
                zahlenlotto_mit_wiederholung(n, k)
            else:
                print("FEHLER: Ziehung darf nicht groesser sein als Auswahl.")

        elif auswahl == 2:
            print("Lottospiel wird beendet.")
            break

        else: 
            print("Falsche Eingabe")


main()


