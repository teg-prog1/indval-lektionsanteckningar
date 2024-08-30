# Kommentarer

# Skrivs med # innan. Bra att kommentera sitt program så att man kommer ihåg vad man har gjort.
# Högst upp i varje fil skriver ni ert namn, vad filen är till för och senast ni ändrade den




# Hello world
# Traditionellt första program
#print används för att skriva ut någonting

#print("Hello world!")


# Variabler

# Vad kan jag döpa min variabel till?
#   siffror, bokstäver, understreck
#   understreck eller stor bokstav
#   något namn som är beskrivande
#   case sensitive
#   vissa ord är "förbjudna"

namn = "Felicia"

namn_syster = "Frida"
namnSyster = "Frida"

#print(namn)

namn = "Therese"

#print(namn)

#Vanligare att skriva variabler med små bokstäver




# Python förstår själv vilken typ variabeln har, man behöver oftast inte definiera det själv.


# Datatyper

#   String
# en string är text, skrivs med "" runt

intresse = "segling" #string

#   Int (heltal)

ålder = 25
tal = -5


#   Float (decimaltal, kom ihåg att använda . istället för ,)

ålder_barn = 5.0


#   Boolean (är antingen sann eller falsk)

glad = True
trött = False


# Input
#inputen blir automatiskt en string, 
# om det ska vara t.ex. en int behöver vi "casta" den till int, det vill säga ändra explicit.


#svar = input("Vad vill du äta?")
#print(svar)

#tal = int(input("Gissa ett tal: "))


tal = tal + 2

#print(tal)







# om vi har + måste vi göra om ökad_ålder till en int
# vi kan också skriva , mellan två saker att printa, då läggs ett mellanslag automatiskt till


# Det är skillnad vad som händer med + beroende på om man jobbar med int eller string


print("Hej, jag heter",namn,"och jag är",ålder)

print("Hej, mitt namn är "+namn)






# två olika sätt att lägga till 23 till ett heltal



#print(tal_addera)
 


# Ta reda på en typ för en variabel



# Räkneoperationer

#   +, -, *, /, //, %, **

# vi kan addera både heltal och decimaltal
test_tal = 9
test_tal_2 = 7

test_tal * test_tal_2


# vi kan subtrahera med både heltal och decimaltal



# vi kan multiplicera med både heltal och decimaltal



# vi kan dividera som vanligt med / Då blir det ett decimaltal om det inte går jämnt ut.

print(test_tal_2/test_tal)


# vi kan göra heltalsdivision, då struntar programmet i decimaler. OBS: programmet avrundar inte

print(test_tal_2//test_tal)

# vi kan få ut resten vid en division. T.ex. blir 10%3 1 eftersom 3 får plats 3 gånger i 10, och det blir 1 över.

print(10%3)



# vi kan höja upp tal i något

print(3**2)



