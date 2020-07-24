age = int(input("Alter der Person angeben: "))

# Lösung nur mit if-else
if age >= 30:
    if age <= 39:
        print("1 - Diese Person ist in ihren 30ern.")
    else:
        print("1 - Diese Person ist nicht in ihren 30ern.")
else:
    print("1 - Diese Person ist nicht in ihren 30ern.")


# Lösung mit and
if age >= 30 and age <=39:
    print("2 - Diese Person ist in ihren 30ern.")
else:
    print("2 - Diese Person ist nicht in ihren 30ern.")

# Lösung mit or
if age < 30 or age >=40:
    print("3 - Diese Person ist nicht in ihren 30ern.")
else:
    print("3 - Diese Person ist in ihren 30ern.")

if False:
    print("if-Abfrage wurde ausgeführt.")