# for-loopar
# range (kolla på w3schools), ni ska kunna läsa den informationen som finns på W3schools
for i in range(10):
    print(i)

# vi kan loopa igenom ett namn till exempel
namn = "Felicia"
for bokstav in namn:
    print(bokstav)

# while-loopar, kör tills något blir falskt
kör_program = True

# En oändlig loop, bryts med ctrl c
#while kör_program:
    #print("hej")

# allt som går att göra med for-loop går att göra med while-loop, men inte tvärtom
# om man ska göra något ett visst antal gånger är det klokt att använda for-loop

# exempel på while-loop som motsvarar den första for-loopen i anteckningarna
tal = 0
while tal < 10:
    print(tal)
    tal += 1

# while-loop som "spelloop"
# till exempel fortsätta fråga tills man har rätt
inte_rätt_svar = True
while inte_rätt_svar:
    svar = input("Vad är 15*2? ")
    if svar == "30":
        inte_rätt_svar = False


# break, kan stoppa en loop också


# nästlade loopar, vi kan ha loopar i varandra
for i in range(5):
    for j in range(5):
        print(i,j)


# Importera random, importerar modulen random, som kan göra massa saker med slump
import random

slumptal = random.randint(1,5) # exempel på att slumpa heltal
print(slumptal)