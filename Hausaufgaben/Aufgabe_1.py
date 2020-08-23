n = int(input("Bitte eine ganze Zahl n eingeben: "))
summe = 0

for i in range(1, n+1):
    # summe = summe + i
    summe += i
    
print("Die Summe der Zahlen von 1 bis {0} ist {1}.".format(n, summe))