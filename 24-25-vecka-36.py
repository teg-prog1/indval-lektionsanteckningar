# if, else, elif

# if, else och elif kan användas för att programmet ska göra olika saker beroende på villkor

# om vi till exempel vill skriva ut olika saker beroende på hur stort ett tal är
#tal = int(input("Säg ett heltal: "))

#if tal > 10:
 #   print("Grattis!")

#elif tal < 5:
  #  print("Hurra!")

#elif tal == 7:
 #   print("Hej!")

#else:
 #   print("hallå!")











# För att markera att något är "inom" if-satsen eller inom elif eller inom else används indenteringar
    # denna rad är exempelvis indenterad jämfört med raden ovan

# jämförelser kan göras exempelvis med dessa:
# <=, <, >, >=, ==, !=
    





# mindre än eller lika med skrivs med <=, och större än eller lika med tvärtom med >=

# att kolla om något inte är lika med görs med ! innan =


# and, or, not
# vi kan kolla två saker samtidigt


#if ålder >= 18 or namn == "Felicia":








# vi kan ha flera elif om vi vill



# nästlade if-satser
# vi kan också ha if-satser i varandra, så kallade nästlade if-satser

#if tal < 3:
    #if namn == "Therese":
        #print("Hej")







#########################################################################################################


# while-loop
# kan användas när man vill köra en kod flera gånger tills något stoppar den
# control c


""" kör = True
tal = 1

while kör:
    print("hej")
    svar = input("Vill du avsluta? ")

    if svar == "ja":
        kör = False
 """








# for-loop
# kan användas när man vill köra en kod ett visst antal gånger, eller loopa igenom en sak (till exempel en sträng)


for i in range(20,3,-1):
    print(i)


# for x in "apple"
    
for bokstav in "apple":
    print(bokstav)



# nästlade for-loopar
# vi kan även ha loopar i loopar, testa själv och se vad som skrivs ut
