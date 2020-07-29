# Klassendefinitionen
class Auto:
    def __init__(self, marke, farbe, leistung, anzahl_tueren): # Methode
        self.kilometerstand = 0 # Attribute
        self.marke = marke
        self.farbe = farbe
        self.leistung = leistung
        self.anzahl_tueren = anzahl_tueren

        print("Neuwagen erstellt.")

    def zeige_daten(self): # Methode
        print("Marke:", self.marke)
        print("Kilometerstand:", self.kilometerstand)
        print("Farbe:", self.farbe)
        print("Leistung:", self.leistung)
        print("Anzahl der Tueren:", self.anzahl_tueren)

    def strecke_fahren(self, kilometer): # Methode
        print("Das Auto faehrt {0} Kilometer".format(kilometer))
        self.kilometerstand += kilometer

# Hauptprogramm
def main():

    auto_eins = Auto("Peugot", "Silber", 100, 3)
    auto_zwei = Auto("VW", "Rot", 55, 4)

    print()
    print("Daten von Auto eins:")
    auto_eins.zeige_daten()

    print()
    print("Daten von Auto zwei:")
    auto_zwei.zeige_daten()

    print("\nDie Autos fahren ein wenig in durch die Gegend ...")

    auto_eins.strecke_fahren(340)
    auto_zwei.strecke_fahren(408)

    print("Kilometerstand des auto_eins:", auto_eins.kilometerstand)
    print("Kilometerstand des auto_zwei:", auto_zwei.kilometerstand)

main()

