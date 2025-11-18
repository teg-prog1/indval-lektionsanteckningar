
# Revisit travelbag, hur fungerar det med listor som parameter

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


# Om strukturen i ett program
# Ha en main-funktion!

# Om default-värden på parametrar

# Om att returnera flera saker från en funktion

# Om lokala och globala variabler (läs s 112-113)

# Varför vill vi undvika globala variabler och vilka variabler är rimliga att ha globala?