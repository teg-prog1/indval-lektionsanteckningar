# len() är en funktion
# vi skickar in en lista, den gör något och ger sen ut en längd
frukter = ["banan", "äpple", "kiwi"]
längd = len(frukter)
print(längd)


# int() är en funktion
# den tar in något (till exempel en sträng), gör något med den och skickar ut en integer
tal = "2354"
tal_som_int = int(tal)
print(tal_som_int)


# En funktion är ett block kod som har ett "namn"

# Exempel: hälsningsfunktion (tar inte in något och returnerar ingenting)
def hälsningsfunktion():
    print("Hejsan!")

hälsningsfunktion() # Här anropar vi funktionen, dvs använder den

# Terminologi att kunna:
# parameter
# argument
# anropa/kalla på funktion
# ”Parameter = parkeringsplatsen, argument = bilen som parkerar där.”

# Exempel: räkna summa (en funktion som har två parametrar)
def summa(tal_1, tal_2):
    resultat = tal_1 + tal_2
    return resultat # funktionen reeturnerar summan, dvs ger tillbaka den


resultat_från_funktion = summa(3,5) # för att vi ska kunna använda returvärdet behöver vi spara det någonstans
print(resultat_från_funktion)



# Exempel: variabler i funktionen är lokala

def test_funktion(x):
    print(f"x är nu inne i funktionen: {x}")
    x += 5
    print(f"Nu är x inne i funktionen: {x}")

x = 4
print(f"Utanför funktionen är x: {x}")
test_funktion(x)
print(f"Nu utanför funktionen är x: {x}")

# Ett tips är att döpa variabeln utanför funktionen till något annat än den variabeln som finns inuti funktionen

# Vad är funktioner bra för?

# Göra samma sak flera gånger (exempel: testa om en input är i rätt spann
def testa_input(svar, lägsta, högsta):
    if lägsta <= svar <= högsta:
        print("Godkänd")
    
    else:
        print("Icke godkänd")

# Strukturera kod (exempel: uppgiften resväska)

def lägg_till_i_resväskan(travelbag):
    sak_att_lägga_till = input("Vad vill du lägga till i din resväska?: ")
    travelbag.append(sak_att_lägga_till)

travelbag = []

while True:
   menyval = input("1. Kolla i resväskan\n2. Lägg sak i resväskan\n3. Ta bort sak i resväskan\n4Avsluta program")

   if menyval == "1":
       pass

   elif menyval == "2":
       lägg_till_i_resväskan(travelbag)
       print(travelbag)

   elif menyval == "3":
       pass

   elif menyval == "4":
       break
