# Radbrytningar i program

# Kommentarer
# Man kan göra kommentarer i sitt program med hjälp av #
# Kommentarerna läses inte som kod, utan kan användas för att förklara och göra anteckningar
# Kommentera gärna varje uppgift med vilken uppgift det är

# Felmeddelanden
# Exempel:
#f = open("demofile.txt")
#print(f.read())
# Lär er att läsa och tolka felmeddelanden, typ av fel, vilken rad


# if-satser, kan användas för att dela upp vad som ska hända i programmet
# indentering
# När man är "inom" en if-sats så är koden indenterad (flyttad lite till höger)
# Indenteringen avgör om man är inom if-satsen eller inte

# Exempel på if-sats med elif och else
ålder = int(input("Hur gammal är du? "))
if ålder >= 18:
    print("Grattis, du är myndig!")

elif ålder < 7:
    print("Du går inte i skolan")

else:
    print("Hej!")


# jämförelser (==,<, >, <=, >=, !=)
# i if-satser använder vi ofta olika villkor, som till exempel de ovan
# == betyder lika med
# < betyder mindre än
# > betyder större än
# <= betyder mindre än eller lika med
# >= betyder större än eller lika med
# != betyder inte lika med


# Exempel med if/elif/else

if ålder >= 65:
    print("Pensionär")

elif ålder >= 20:
    print("vuxen")

elif ålder >= 18:
    print("myndig")

else:
    print("Hej!")


# Kan man inte ha bara massa if istället för elif?
# Det beror på vad man vill göra
# Om man har if så står de för sig själva, det blir en helt ny utvärdering
# Om man har elif så hör den ihop med if och elif innan
 


# booleans
# en datatyp som är antingen sann eller falsk
kör_programmet = True
glatt_humör = False


if kör_programmet:
    print("hej")

# and, or, not kan användas för att utvärdera flera villkor
# prioriteringsregler med and/or, använd parenteser för att få det rätt!

tal1 = 10
tal2 = 8

if tal1 < 20 or (tal2 > 5 and tal1 + tal2 == 18):
    print("hurra!")

# nästlade if-else, vi kan ha if/elif/else inuti andra if/elif/else
if tal2 < 30:
    if tal2 >10:
        print("Hej")
    else:
        print("hallå")
else:
    print("hejdå")


