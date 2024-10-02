############## DICTIONARY #############

# Skrivs med {} och har par av nyckel och värde
# Ordnade, går att ändra, tillåter inte dubletter (inte samma nyckel)


ålder_data = {"Felicia":25 , "Frida":23 , "Victor":26, "Mikaela":25}

# Kan innehålla olika datatyper
intressen = {"Felicia":["segla","pussla","resa"] , "Victor":["laga mat","resa","programmera"]}


# Skriva ut ett värde från en nyckel

ålder_felicia = ålder_data["Felicia"]
print(ålder_felicia)

felicia_intresse_1 = intressen["Felicia"][0]
print(felicia_intresse_1)

# Skillnad på tom dictionary och tom mängd (set)
ny_dict = {}
nytt_set = set()

# Metoder för dictionary: https://www.w3schools.com/python/python_dictionaries_methods.asp

# Att kopiera en lista
# Det första sättet kommer inte att fungera, då variablerna test_lista och ny_lista bara pekar på samma ställe i minnet
test_lista = [1,2,3,4,5,6]
ny_lista = test_lista
ny_lista.append(8)
print(test_lista)
print(ny_lista)

# Istället får vi använda metoden copy() för att faktiskt få en kopia
kopia_lista = test_lista.copy()
kopia_lista.append(9)
print("__________________________________")
print(test_lista)
print(kopia_lista)


############## FÅNGA FEL #############
# fånga när programmet kraschar eller när vi själva vill fånga något fel som inte är en krasch
try: # Vi testar att köra koden nedan
    tal = int(input("skriv in ett tal! ")) # om man inte skriver ett heltal så blir det ValueError
    if tal < 0:
        raise ValueError # om talet är negativt så vill vi att det också ska bli ValueError
    print(tal)

except ValueError: # om koden under try blir ValueError så körs istället den här koden
    print("du skrev inte ett positivt heltal!")
    print("instruktion")
