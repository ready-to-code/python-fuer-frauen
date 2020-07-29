class Automobil(object):
    antrieb = "Ottomotor"
    leistung_in_kw = 120.0

    def ausgabe(self):
        print("Antrieb:", self.antrieb)
        print("Leistung:", self.leistung_in_kw)

class PKW(Automobil):
    pass

print("Werte fuer Bus")
bus = Automobil()
bus.ausgabe()

print("\nWerte fuer Smart")
smart = PKW()
smart.ausgabe()
