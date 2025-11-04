# len() är en funktion


# int() är en funktion


# En funktion är ett block kod som har ett "namn"

# Exempel: hälsningsfunktion (tar inte in något och returnerar ingenting)


# Terminologi
# parameter
# argument
# anropa/kalla på funktion
# ”Parameter = parkeringsplatsen, argument = bilen som parkerar där.”

# Exempel: räkna summa (en funktion som har två parametrar)


# Exempel: variabler i funktionen är lokala
'''
def test_funktion(x):
    print(f"x är nu inne i funktionen: {x}")
    x += 5
    print(f"Nu är x inne i funktionen: {x}")

x = 4
print(f"Utanför funktionen är x: {x}")
test_funktion(x)
print(f"Nu utanför funktionen är x: {x}")
'''

# Exempel: en funktion som returnerar något (bara en sak)


# Hur använder vi returvärdet (jämför med input())
# Måste spara det som returneras i en variabel

# Vad är funktioner bra för?

# Göra samma sak flera gånger (exempel: testa om en input är i rätt spann


# Strukturera kod (exempel: uppgiften resväska)
'''
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
'''