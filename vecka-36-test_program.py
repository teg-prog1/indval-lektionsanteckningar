
import random

for i in range(8):
    random_tal = random.randint(0,100)
    print("Rätt tal:", random_tal)
    gissa = int(input("Gissa ett tal mellan 0-100"))
    if gissa == random_tal:
        print("Rätt")
    else:
        print("Fel")