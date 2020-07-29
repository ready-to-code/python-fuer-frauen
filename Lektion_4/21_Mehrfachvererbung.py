class PKW(object):
    sitzplaetze = 5

    def ausgabePKW(self):
        print("Sitzplaetze: ", self.sitzplaetze)

class LKW(object):
    ladeflaeche = 6.0

    def ausgabeLKW(self):
        print("Ladeflaeche in qm: ", self.ladeflaeche)

class Pick_Up(PKW, LKW):
    motorleistung = 120.0

    def ausgabe(self):
        self.ausgabePKW()
        self.ausgabeLKW()
        print("Motorleistung in KW: ", self.motorleistung)

a = Pick_Up()
a.ausgabe()