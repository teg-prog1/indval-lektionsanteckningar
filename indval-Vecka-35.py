# Kommentarer

# Skrivs med # innan. Bra att kommentera sitt program så att man kommer ihåg vad man har gjort.
# Högst upp i varje fil skriver ni ert namn, vad filen är till för och senast ni ändrade den

# Felicia Rosenberg - Genomgång vecka 35, ändrad 30/8-2023

# Hello world
# Traditionellt första program
#print används för att skriva ut någonting
print("Hello, World!")

# Variabler

# Vad kan jag döpa min variabel till?
#   siffror, bokstäver, understreck
#   understreck eller stor bokstav
#   något namn som är beskrivande
#   case sensitive
#   vissa ord är "förbjudna"

namn = "Felicia"
lillasyster_namn = "Frida"
lillasysterNamn = "Frida"

#Vanligare att skriva variabler med små bokstäver

# Python förstår själv vilken typ variabeln har, man behöver oftast inte definiera det själv.

ålder = 24

# Datatyper

#   String
# en string är text, skrivs med "" runt
mening = "Vädret idag är halvklart.\nDet borde vara mer sol."
#print(mening)

#   Int (heltal)

ett_tal = -3

#   Float (decimaltal, kom ihåg att använda . istället för ,)

ett_decimaltal = 3.4

#   Boolean (är antingen sann eller falsk)

ätit_middag = False
ätit_lunch = True


# Input
#inputen blir automatiskt en string, 
# om det ska vara t.ex. en int behöver vi "casta" den till int, det vill säga ändra explicit.

svar = int(input("Hur gammal är du?"))
print(svar)
ökad_ålder = svar + 5

# om vi har + måste vi göra om ökad_ålder till en string
# vi kan också skriva , mellan två saker att printa, då läggs ett mellanslag automatiskt till
print("Här är din ålder plus 5: " + str(ökad_ålder))
print("Här är din ålder plus 5:",ökad_ålder)

# Det är skillnad vad som händer med + beroende på om man jobbar med int eller string
print(str(8)+str(5))
print(8+5)


# två olika sätt att lägga till 23 till ett heltal

tal_addera = 7
summa = tal_addera + 1
tal_addera = tal_addera + 1
tal_addera += 1

#print(tal_addera)


# 


# Ta reda på en typ för en variabel

hungrig = True
print(type(hungrig))

# Räkneoperationer

#   +, -, *, /, //, %, **

# vi kan addera både heltal och decimaltal

print(9.7+11.4)
print(9.7+7)
print(9+2)

# vi kan subtrahera med både heltal och decimaltal

print(9.7-11.4)
print(9.7-7)
print(9-2)

# vi kan multiplicera med både heltal och decimaltal

print(9.7*11.4)
print(9.7*7)
print(9*2)

# vi kan dividera som vanligt med / Då blir det ett decimaltal om det inte går jämnt ut.

print(11/3)

# vi kan göra heltalsdivision, då struntar programmet i decimaler. OBS: programmet avrundar inte
print(11//3)

# vi kan få ut resten vid en division. T.ex. blir 10%3 1 eftersom 3 får plats 3 gånger i 10, och det blir 1 över.

print(10//3,10%3)

# vi kan höja upp tal i något
print(9**2)

# Importera random


import random

print(random.randint(1,6))




