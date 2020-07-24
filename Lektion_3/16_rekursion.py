# Verwenden einer Funktion innerhalb derselben Funktion

# Countdown
def countdown(wert):
    print("Countdown:", wert)

    if wert > 0:
        countdown(wert-1)

countdown(10)