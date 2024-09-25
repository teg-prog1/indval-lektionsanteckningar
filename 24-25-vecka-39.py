# Funktioner

# Ett block med kod som kan användas på andra ställen i programmet

# En funktion har ett namn och behöver definieras


def hälsning():
    print("Hej!")


# För att köra en funktion behöver vi kalla på den. Först definierar vi bara den, sen kan vi använda den.
hälsning()

# Vi kan använda den flera gånger om vi vill.
hälsning()

# En funktion kan ta in en parameter som den kan använda. Det kan vara vilken slags variabel som helst.
def personlig_hälsning(namn1, namn2=""):
    print(f"Hej {namn1} och {namn2}!")

person_namn = "Felicia"
personlig_hälsning(person_namn)

# Funktioner kan också ta in flera parametrar

# Om man skriver in för många eller för få parametrar blir det fel

# Vi kan ha en default också om vi vill, då behövs inte parametern


# Funktionen kan returnera något

def statistik(tal1,tal2):
    summa_resultat = tal1 + tal2
    medel = summa_resultat/2
    return summa_resultat,medel

summa, medelvärde = statistik(3,7)
print(summa)
print(medelvärde)

# Om vi vill spara det som returneras måste vi lägga det i en variabel

# Det går att returnera flera saker från en funktion.


# Ett till exempel på funktion

def kolla_tal(tal):
    if 1 <= tal <= 10:
        return True
    else:
        return False

svar = int(input("Säg ett tal som är mellan 1-10"))
if kolla_tal(svar):
    print("rätt")













