
# fyra datatyper hittills, int, float, bool, string
# string är itererbar = går att loopa  igenom
namn = "Felicia"
for bokstav in namn:
    print(bokstav)

# lista, element
# en lista skapas med hakparenteser []
# varje sak i listan är ett element
frukter = ["banan", "äpple", "päron", "ananas"]


# en lista är ordnad, det vill säga elementen kommer att stanna kvar i den ordning de läggs till
#varje element i listan har ett index, vi börjar räkna på 0
print(frukter[1])

# går att förändra, vi kan förändra element i listan och ta bort och lägga till och sortera om
frukter[0] = "granatäpple"

# vi kan ha olika datatyper i listor
blandad_lista = [2.4, 65, "hej", True, [1,2,3]]

# loopa igenom lista med for-loop
for element in blandad_lista:
    print(element)

# slicea listor, som att slicea strängar
frukter = ["banan", "granatäpple", "äpple", "päron", "ananas", "apelsin", "lime", "citron"]
print(frukter[1:5:2])

# listomfattningar (list comprehensions), ett sätt att väldigt effektivt skapa listor
newlist = [tal**2 for tal in range(0,85) if tal%2==0] # skapar en lista med kvadrater av jämna tal

# Raderna nedan skapar exakt samma lista med kvadrater, men med en vanlig loop istället
newlist = []
for tal in range(0,85):
    if tal%2 == 0:
        newlist.append(tal**2)

# Ett annat exempel på listomfattning
new_list_2 = [tal_1*tal_2 for tal_1 in range(1,4) for tal_2 in range(1,3)]

new_list_2 = []
for tal_1 in range(1,4):
    for tal_2 in range(1,3):
        new_list_2.append(tal_1*tal_2)

# Listmetoder, inbyggda saker man kan göra med listor
# len()
längd_på_lista = len(frukter)
print(längd_på_lista)

# append()
print(frukter)
frukter.append("kiwi")

# sort() och sorted()
frukter.sort() # sorterar om orginallistan
print(frukter)

nya_frukter = sorted(frukter) # skapar en ny version av listan som är sorterad
print(frukter)
print(nya_frukter)

# andra metoder på w3shools

# Lista med listor, matris. Blir som en tvådimensionell lista, ett rutnät
matris = [[1,4,7],[3,4,9],[9,4,7]]
print(matris[2][0])


# tipplar/ tuples, en annan liknande datatyp
vokaler =("a","o","å","e","i","y","ä","ö")

# tuples är oföränderliga, det går itne att ändra element, lägga till, ta bort eller ändra ordning

# ordnad precis som listor

# packa upp en tuple = lägga ut värdena i separata variabler
info_tuple = ("Felicia", 26)
namn, ålder = info_tuple
print(namn)
print(ålder)

# packa in tuple, lägga in variabler i en tuple
stad = "Stockholm"
temperatur = 13
info_om_plats = (stad,temperatur)

#######################################################################################################################


# Skapa ett nytt variabelnamn som refererar till samma lista
# En kopia skapas inte, utan vi skapar bara ett till variabelnamn som  refererar till samma lista
namn_lista = ["Felicia", "Frida", "Max", "Patrik", "Kamilla", "Victor"]
annan_lista = namn_lista
annan_lista.append("August")
print(namn_lista)


# Kopiera en lista på tre sätt

# kopiera med for-loop
annan_lista = []
for person in namn_lista:
    annan_lista.append(person)

# kopiera med listomfattning
annan_lista = [person for person in namn_lista]

# kopiera med slice (mest effektivt)
annan_lista = namn_lista[:]

# Platser i minnet som inget refereras till längre tas omhand genom Pythons garbage collect
