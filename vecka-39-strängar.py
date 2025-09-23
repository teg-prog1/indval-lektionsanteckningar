# OLIKA CITATIONSTECKEN

# vi kan ha vanliga dubbla citattecken

# vi kan ha enkla (samma tangent som *)

# Vi kan också ha trippla (tre stycken enkla)
# Då kan man ha radbrytningar och citattecken inuti strängen
'''tal = 3
if tal%5 == 0:
    print("Woho!")'''

# Trippla citattecken kan också användas som kommentarer
'''Det här blir som en kommentar'''

# STRÄNGAR ÄR ITERERBARA
# De är lagrade som en följd av tecken i minnet
# vi börjar räkna från 0, detta kommer att skriva ut första tecknet
namn = "Felicia"
print(namn[0])
print(namn[3])

# Vi kan loopa igenom en sträng
for tecken in namn:
    print(tecken)

# Vi kan kolla om bokstäver finns i strängen
if "c" in namn:
    print("Det finns ett c!")


#IMMUTABLE
# Strängar i python är immutable (oföränderliga)
# Det betyder att vi inte kan ändra innehållet på följande sätt
#namn[0] = "G" # gör inte att strängen blir Gelicia istället, istället blir det ett felmeddelande
    
# JÄMFÖRA STRÄNGAR
# Vi kan jämföra strängar precis som tal med == och !=
# == kollar om strängarna är exakt lika
# != kollar om de är olika

if "Felicia" != "felicia":
    print("Hallå!")



# BITAR AV STRÄNGAR
# Vi kan ta fram bitar av en sträng (kallas för att slicea (engelska: slice))
lång_sträng = "Hej Felicia, hoppas du mår bra idag!"
print(lång_sträng[1:12:2]) # börjar på index 1 och slutar på 12 (men tar inte med 12),
                            # den sista 2:an anger att vi ska gå varannat tecken
print(lång_sträng[::-1]) # börjar på 0 och går genom hela strängen, går med steg -1, dvs baklänges


# STRÄNGMETODER
# Vi kan göra massa saker med strängar, det finns en lista på w3Schools över strängmetoder
# https://www.w3schools.com/python/python_strings_methods.asp

# Kolla längden på en sträng
print(len(namn))

#även mellanslag och andra specialtecken räknas

# räkna förekomsten av en delsträng
# count()
print(namn.count("i"))

# göra så att bokstäver är stora/små
# upper()
# lower()
print(namn.upper())

# Finns massa fler metoder, ni får själva testa olika i uppgifterna