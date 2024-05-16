#########  Uppgift 1  ############

namn = "Felicia"
intresse1 = "segla"
intresse2 = "läsa"

print(namn, " gillar att ", intresse1, " och ", intresse2)


#########  Uppgift 2  ############

födelseår = 1998
ålder_nu = 2024-1998
print(ålder_nu)


#########  Uppgift 3  ############

namn = input("Vad heter du?")
ålder = int(input("Hur gammal är du?"))
år_till_pension = 65-ålder

print("Hej ", namn, " du har ", år_till_pension, " år kvar till pension")


#########  Uppgift 4  ############

antal_rätt = 0

# första frågan
svar1 = input("När startades TEG?")
if svar1 == "1999":
    print("Rätt")
    antal_rätt = antal_rätt + 1
else:
    print("Fel")

# andra frågan
svar2 = input("Hur många klasser går på TEG nu?")
if svar2 == "33":
    print("Rätt")
    antal_rätt = antal_rätt + 1
else:
    print("Fel")

# tredje frågan
svar3 = input("Vad heter hon som jobbar som vikarie på TEG?")
if svar3 == "Klara":
    print("Rätt")
    antal_rätt = antal_rätt + 1
else:
    print("Fel")

# fjärde frågan
svar4 = input("Vem är VD på TEG?")
if svar4 == "Fredrik":
    print("Rätt")
    antal_rätt = antal_rätt + 1
else:
    print("Fel")

print("Du hade ", antal_rätt, " rätt av 4 frågor")


#########  Uppgift 5  ############

#Att-göra lista
att_göra_lista = [] #Här definieras en tom lista


while True:
  menyval = input("1. Kolla i listan\n"
                  "2. Lägg till sak i listan\n"
                  "3. Ta bort sak från listan\n"
                  "Avsluta program")


  if menyval == "1":
      print("Det här finns i din lista:")
      for sak in att_göra_lista:
          print(sak)


  elif menyval == "2":
      sak_att_lägga_till = input("Vad vill du lägga till i listan?")
      att_göra_lista.append(sak_att_lägga_till)


  elif menyval == "3":
      plats_att_ta_bort = input("Från vilken plats vill du ta bort från listan?")
      att_göra_lista.pop(plats_att_ta_bort)


  elif menyval == "4":
      break



#########  Uppgift 6  ############

# DEL 1:
namn_biljett = input("Vad heter du?")
ålder_biljett = int(input("Hur gammal är du?"))

if ålder < 11:
    biljett_pris = 20

elif ålder > 65:
    biljett_pris = 25

else:
    biljett_pris = 40

print("------------------")
print("    Biljett SL    ")
print("    Pris: ", biljett_pris)
print("    Namn: ", namn_biljett)

# DEL 2:
antal_biljetter_barn = int(input("Hur många biljetter till barn vill du köpa?"))
antal_biljetter_pensionär = int(input("Hur många biljetter till pensionärer vill du köpa?"))
antal_biljetter_vuxen = int(input("Hur många biljetter till vuxna vill du köpa?"))

#Barnen
for i in range(antal_biljetter_barn):
    namn_barn = input("Vad heter barnet?")
    print("------------------")
    print("    Biljett SL    ")
    print("    Pris: 20 kr")
    print("    Namn: ", namn_barn)

#Pensionärerna
for j in range(antal_biljetter_pensionär):
    namn_pensionär = input("Vad heter pensionären?")
    print("------------------")
    print("    Biljett SL    ")
    print("    Pris: 25 kr")
    print("    Namn: ", namn_pensionär)

#De vuxna
for k in range(antal_biljetter_barn):
    namn_vuxen = input("Vad heter den vuxna?")
    print("------------------")
    print("    Biljett SL    ")
    print("    Pris: 40 kr")
    print("    Namn: ", namn_vuxen)

#########  Uppgift 7  ############

#Del 1
for i in range(10):
    print("Hej")
    
#Del 2
for i in range(7):
    print(i)
    
#Del 3
for j in range(13,38):
    print(j)
    
#Del 4
for k in range(4,21,2): # 4 är start, 21 gör att 20 är slut, 2 är antal steg den hoppar
    print(k)

#Del 5
for h in range(20,-1,-1):
    print(h)


#########  Uppgift 8  ############

while True:
    svar = input("Vilket djur ser bra?")
    if svar == "zebra":
        break


# Alternativ lösning:
svar = ""

while svar != "zebra":
    svar = input("Vilket djur ser bra?")


#########  Uppgift 9  ############

for i in range(101):
    if i%3 == 0:
        print("Fizz")
    else:
        print(i)
