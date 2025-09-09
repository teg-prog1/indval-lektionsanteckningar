# Radbrytningar i program

# Kommentarer, vad är en bra kommentar

# Hur ska en uppgift se ut när ni har gjort den?


# Felmeddelanden
# Exempel:
#f = open("demofile.txt")
#print(f.read())
# Lär er att läsa och tolka felmeddelanden, typ av fel, vilken rad

# Övning felmeddelanden


# Tips om w3schools, länk finns i lektionsloggen


# if
# indentering
#ålder = int(input("Hur gammal är du? "))
#if ålder >= 18:
 #   print("Grattis, du är myndig!")

#elif ålder < 7:
    #print("Du går inte i skolan")

#else:
  #  print("Hej!")


# jämförelser (==,<, >, <=, >=, !=)


# else
# elif

#if ålder >= 65:
    #print("Pensionär")

#elif ålder >= 20:
    #print("vuxen")

#elif ålder >= 18:
  #  print("myndig")

#else:
 #   print("Hej!")


# Kan man inte ha bara massa if istället för elif?
 


# pass
#namn = input("Vad heter du? ")
#if namn == "Felicia":
 #   print(f"Hej {namn}")
#else:
 #   pass


# booleans
#kör_programmet = True
#glatt_humör = False

#if kör_programmet == True:
 #   print("hej")

#if kör_programmet:
 #   print("hej")

#mående = input("Hur mår du? ")
#if mående == "bra":
 #   print("Hurra!")


# bool == True

# jämförelser blir booleans

# and, or, not (inte xor)
# prioriteringsregler med and/or

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


