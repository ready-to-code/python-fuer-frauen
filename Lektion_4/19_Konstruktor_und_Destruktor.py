class beispiel(object):
    def __init__(self):  # Konstruktor
        print("Der Konstruktor wird aufgerufen.")

    def __del__(self):  # Destruktor
        print("Der Destruktor wird aufgerufen.")

a = beispiel()
b = beispiel()

# Objekte löschen
del a
del b

# Objekt a und b wurden gelöscht
print(a)
#b