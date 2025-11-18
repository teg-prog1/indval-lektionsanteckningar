
# Påminnelse om funktioner

def summa(tal_1, tal_2):
    resultat = tal_1 + tal_2
    return resultat

resultat_från_funktion = summa(4,7)
#print(resultat_från_funktion)


# Revisit travelbag, hur fungerar det med listor som parameter
# När vi har listor, tipplar eller dictionarys (som ni får lära er snart) som argument är det lite speciellt
# Det vi skickar in i funktionen är en referens till platsen i minnet där listan ligger
# (ni kanske kommer ihåg att det är lite knepigt att kopiera listor)
# Det innebär att om vi ändrar listan (eller tippeln/dictionaryn) inuti en funktion behöver vi inte returnera den
# Vi har nämligen ändrat själva listan på den platsen i minnet
# Dock med heltat, floats, booleans och strängar behöver vi returnera dem om de har ändrats och vi vill att de ska vara ändrade utanför funktionen
'''
def lägg_till_i_resväskan(travelbag_i_funktion):
    sak_att_lägga_till = input("Vad vill du lägga till i din resväska?: ")
    travelbag_i_funktion.append(sak_att_lägga_till)

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
# Om strukturen i ett program
# Ha en main-funktion!
# Struktur:
# 1. definiera alla funktioner i den ordning de används
# 2. definiera main-funktionen, som är en funktion som kör huvudprogrammet
#    main-funktionen har inga parametrar och returnerar inget
# 3. anropa main-funktionen

# exempel: miniräknare

def summa(tal_1, tal_2):
    resultat = tal_1 + tal_2
    return resultat

def produkt(tal_1, tal_2):
    resultat = tal_1 * tal_2
    return resultat

def main():
    tal_1_in = input("Skriv ett heltal: ")
    tal_2_in = input("Skriv ett till heltal: ")
    val = input("Vill du addera eller multiplicera? ")

    if val == "addera":
        svar = summa(tal_1_in, tal_2_in)
    elif val == "multiplicera":
        svar = produkt(tal_1_in, tal_2_in)

    print(f"Svaret är: {svar}")

main()

# Om default-värden på parametrar
# Vi kan ha default-värden på parametrar om vi vill
# Om man då inte skickar in ett värde för den parametern kommer det att bli default-värdet

def hälsning_baserat_på_ålder(ålder=18):
    if ålder == 18:
        print("Hallå!")
    elif ålder == 20:
        print("Goddag")
    else:
        print("Hej!")

hälsning_baserat_på_ålder()

# Om att returnera flera saker från en funktion

def min_och_max(lista):
    max_värde = max(lista)
    min_värde = min(lista)

    return min_värde, max_värde # vi returnerar flera saker med hjälp av kommatecken mellan

resultat_tuple = min_och_max([1,2,6,7,10]) # resultatet från. return blir automatiskt en tippel/tuple

min_resultat, max_resultat = min_och_max([1,5,2,8,9]) # vi kan packa upp tippeln i flera variabler om vi vill
print(min_resultat)
print(max_resultat)

# Om lokala och globala variabler (läs s 112-113) (se länk i lektionslogg)

# Varför vill vi undvika globala variabler och vilka variabler är rimliga att ha globala?

# Vi vill inte ha globala variabler som någon annan kan råka ändra på
# Vissa variabler som används i hela programmet kan vara globala, men om du är osäker så undvik globala variabler helt