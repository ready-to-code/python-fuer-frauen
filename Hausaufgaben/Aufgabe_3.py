n = int(input("Bitte eine ganze Zahl n eingeben: "))
i = 1
summe = 0

while i <= n:
    summe += i
    i += 1
    
print("Die Summe der Zahlen von 1 bis {0} ist {1}.".format(n, summe))