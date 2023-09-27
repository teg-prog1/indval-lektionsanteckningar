# Funktioner

# Ett block med kod som kan användas på andra ställen i programmet

# En funktion har ett namn och behöver definieras

def hälsning():
    print("Hejsan!")

#hälsning()

# För att köra en funktion behöver vi kalla på den. Först definierar vi bara den, sen kan vi använda den.
# Vi kan använda den flera gånger om vi vill.

# En funktion kan ta in en parameter som den kan använda. Det kan vara vilken slags variabel som helst.

def bättre_hälsning(namn):
    print("Hejsan", namn)

användare = "Felicia"
#bättre_hälsning(användare)

# Funktioner kan också ta in flera parametrar

def addera_tal(tal1, tal2, tal3=9):
    print(tal1+tal2+tal3)

#addera_tal(8,9,10)

# Om man skriver in för många eller för få parametrar blir det fel
#addera_tal(5,4)

# Vi kan ha en default också om vi vill, då behövs inte parametern

# Funktionen kan returnera något

def mulitiplicera(tal1,tal2):
    produkt = tal1 * tal2
    return produkt

resultat = mulitiplicera(8,9)
print(resultat)
print(mulitiplicera(8,7))

# Om vi vill spara det som returneras måste vi lägga det i en variabel

# Det går att returnera flera saker från en funktion.

def dividera_kvadrera(tal1,tal2): # Tar in två heltal. Dividerar två tal med varandra och kvadrerar det första talet.
    kvot = tal1/tal2
    kvadrat = tal1 ** 2
    return kvot, kvadrat

kvot_svar, kvadrat_svar = dividera_kvadrera(16,4)
print(kvot_svar)
print(kvadrat_svar)