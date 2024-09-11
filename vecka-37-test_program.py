# Skriv ett program som frågar användaren efter ett ord som är 3-6 bokstäver långt. 
# När användaren har skrivit in ordet ska programmet skriva ut varje bokstav i ordet på en egen rad.

# Om användaren skriver in ett ord som är för långt eller för kort ska programmet säga ifrån
# och ge användaren ett nytt försök.

# När ordet är utskrivet ska programmet tala om att det är klart.
# Användaren ska sedan få en till chans att skriva in ett nytt ord.
kör_loop = True

while kör_loop:

    svar = input("Skriv in ett or som är 3-6 bokstäver långt: ")

    if 2 < len(svar) < 7:
        for bokstav in svar:
            print(bokstav)

        print("Nu är det klart! :)")
        avsluta = input("Vill du avsluta?")
        if avsluta == "ja":
            kör_loop = False

    else:
        print("Ditt ord är för långt eller för kort")
