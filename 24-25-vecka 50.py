# Skriv ett program som utifrån en mening kan plocka ut alla ord som har fler än 3 vokaler. 
# Programmet ska sedan skriva ut de orden på en rad efter varandra, med radbrytning mellan

# Programmet ska ha en funktion som tar in meningen som parameter och 
# returnerar en lista med de ord som ska skrivas ut

# Det ska finnas en huvudfunktion som hanterar input och output
# Det enda som ska hända när programmet körs är att huvudfunktionen kallas

# Inga globala variabler får finnas

# 1. Sammanfatta kraven, inklusive datatyper
# 2. Hur fungerar funktioner med argument och return?
# 3. Algoritmen, vad ska hända i vilken ordning
# 4. Skriv programmet
# 5. Följ koden och se hur den fungerar
# 6. Testa ordentligt

def testa_mening(mening):
    vokaler = ("a", "o", "u","å","e","i","y","ä","ö")
    mening_uppdelad = mening.split()
    lista_med_ord = []
    for ordet in mening_uppdelad:
        antal_vokaler = 0
        for bokstav in ordet:
            if bokstav in vokaler:
                antal_vokaler += 1
        if antal_vokaler > 3:
            lista_med_ord.append(ordet)

    return lista_med_ord

def main():
    input_mening = input("Skriv in en mening: ")
    lista_att_skriva_ut = testa_mening(input_mening)
    for element in lista_att_skriva_ut:
        print(element)

main()

