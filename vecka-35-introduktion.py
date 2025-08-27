### UPPSTART OCH MATEMATISKA OPERATIONER ###

# print
print("Hello world!") 
# viktigt att skriva exakt såhär, inget mellanslag mellan print och parentes

# +, -, *, /
# De vanligaste räknesätten är likadana som i matematik
# De fungerar bra på både flyttal och heltal
print(4+7)
print(5-1)
print(3*4)
print(9/3)

# modulo, %
# ger resten vid en division
print(10%3) # ger resten vid division av 10 med 3, dvs det blir 1
print(76125743%3) # oavsett tal kommer resten vid division med 3 alltid att bli 0, 1 eller 2

# heltalsdivision, //
# tar bort decimalerna, avrundar INTE
print(10//3)
print(2//3)


# upphöjt i, **
print(9**2)

### HELTAL OCH FLYTTAL ###

# heltal = integer (int)
# går snabbare att räkna med
# representeras med binära tal


# flyttal = float
# decimaltal, med punkt eftersom att Python är amerikanskt



# går att blanda heltal och flyttal i beräkningar
# det som händer då är att Python helt enkelt tolkar heltalet som ett flyttal
print(0.7+1.3)
print(8/4) # en division ger alltid ett flyttal


### VARIABLER ###

# Refererar till något i datorns minne, som en låda
# Tilldelar ett värde till variabeln
ålder = 26

# Vill ha beskrivande variabelnamn, till skillnad från matematiken
namn_på_syster = 5

# Vissa namn är förbjudna
# Får ej börja med siffror, innehålla vissa specialtecken eller vara ett reserverat ord

# Python klarar å, ä och ö

# Håll er till ett språk, engelska eller svenska

# Håll er till en stil, snake_case eller camelCase
syster_ålder = 65
systerÅlder = 65
barn_ålder = 5.5


# Omvandla mellan flyttal och heltal (cast)
float_syster_ålder = float(syster_ålder)
print(float_syster_ålder)
int_barn_ålder = int(barn_ålder)
print(int_barn_ålder)

# Ändra värde på variabel
antal_rum = 5
antal_rum = antal_rum + 1 # vi kan lägga till 1 till antal_rum såhär
antal_rum += 1 # vi kan även göra såhär

# Python är case-sensitive, dvs vi Print är inte samma som print

# Dynamiskt typat och statiskt typat
# Python är dynamiskt typat
# dvs vi behöver inte sätta en datatyp direkt, Python löser det när programmet körs



### STRÄNGAR ###

# En datatyp, är vanlig text
namn = "Felicia Hultén Mattsson"

# Strängar som tal och tal som strängar
antal_kurser = 5
str_antal_kurser = str(antal_kurser) # vi kan göra om heltal till sträng

# om vi lägger ihop strängar blir det annorlunda än om vi lägger ihop heltal
print(antal_kurser+antal_kurser)
print(str_antal_kurser+str_antal_kurser)

klassrum = "242"
int_klassrum = int(klassrum) # vi kan göra om strängar till heltal om de går att göra till heltal
print(int_klassrum)

# Starkt typat: kan inte blanda datatyper i beräkningar
# Svagt typat: kan blanda datatyper i beräkningar
# Python är starkt typat
# Jämför med dynamiskt typat och statiskt typat
antal_katter = 5
antal_hundar = "2"
#summa = antal_katter + antal_hundar #FUNKAR EJ


# Slå ihop strängar med + (konkatenera)
syster_namn = "Frida"
sammanlagda_namn = namn  + syster_namn # att slå ihop strängar kallas konkatenera
#print(sammanlagda_namn)


### UTSKRIFTER ###

# Skriva ut flera saker på två sätt
print("Hej", namn) # vi kan göra med kommatecken
print("Hej "+ namn) # vi kan göra med +, men bara om allt är strängar

# Skriva ut radbrytningar, citattecken och liknande
print("\"\nHallå\tdär!") # backslash används för att skriva ut vissa specialtecken

# Skriva ut med formatering, för att skriva ut variabel inne i en sträng
print(f"Hej där {namn} och {syster_namn}, hur mår ni idag?")

### INMATNINGAR ###

# input(), för att ta in saker från användaren
print("Vad är ditt intresse?")
intresse = input()

intresse_två = input("Vad är ditt andra intresse?")

print(f"Vad kul att du tycker om att {intresse} och {intresse_två}")


# Omvandla input till tal
# Input resulterar alltid i sträng, om det ska vara ett tal så måste vi casta det
antal_syskon = int(input("Hur många syskon har du? "))
print(antal_syskon+9)

