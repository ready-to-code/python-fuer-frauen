n = int(input("Bitte eine ganze Zahl n eingeben: "))
fakultaet = 1

for i in range(1, n+1):
    # fakultaet = fakultaet * i
    fakultaet *= i
    
print("Die Fakultaet der Zahl {0} ist {1}.".format(n, fakultaet))