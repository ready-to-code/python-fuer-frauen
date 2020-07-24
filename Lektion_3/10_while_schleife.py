print("Menue:")
print("1: Heizstab ein")
print("2: Heizstab aus")
print("3: Programm beenden")

# aktion = 0

while aktion != 3:
    aktion = int(input("Aktion wählen:"))

    # Funktion ausführen
    if aktion == 1:
        print("Heizstab wird eingeschaltet")
    elif aktion == 2:
        print("Heizstab wird ausgeschaltet")
    elif aktion == 3:
        print("Programm wird beendet")
    else:
        print("Ungültige Eingabe")


# while-else-Schleife
abbruch = int(input("Abbruch des Zaehlers bei: "))

zaehler = 0

while zaehler <= 10:
    if zaehler == abbruch:
        print("Zähler abgebrochen")
        break

    zaehler += 1
    print(zaehler)
else:
    print("Zaehler erfolgreich beendet.")
