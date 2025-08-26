### UPPSTART OCH MATEMATISKA OPERATIONER ###

# print
print("Hello world!")

# +, -, *, /
#print(4+7)
#print(5-1)
#print(3*4)
#print(9/3)

# modulo, %
#print(10%3)
#print(76125743%3)

# heltalsdivision, //
# tar bort decimalerna, avrundar INTE
#print(10//3)
#print(2//3)


# upphöjt i, **
#print(9**2)

### HELTAL OCH FLYTTAL ###

# heltal = integer (int)
# går snabbare att räkna med
# representeras med binära tal


# flyttal = float
# decimaltal, med punkt eftersom att Python är amerikanskt



# går att blanda heltal och flyttal
#print(0.7+1.3)
#print(8/4)


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
#print(float_syster_ålder)
int_barn_ålder = int(barn_ålder)
#print(int_barn_ålder)

# Ändra värde på variabel (+= osv)
antal_rum = 5
antal_rum = antal_rum + 1
antal_rum += 1

# Python är case-sensitive

# Dynamiskt typat och statiskt typat
# Python är dynamiskt typat
# dvs vi behöver inte sätta en datatyp direkt



### STRÄNGAR ###

# En datatyp
namn = "Felicia Hultén Mattsson"

# Strängar som tal och tal som strängar
antal_kurser = 5
str_antal_kurser = str(antal_kurser)
#print(antal_kurser+antal_kurser)
#print(str_antal_kurser+str_antal_kurser)

klassrum = "242"
int_klassrum = int(klassrum)
#print(int_klassrum)

# Starkt typat: kan inte blanda datatyper i beräkningar
# Svagt typat: kan blanda datatyper i beräkningar
# Python är starkt typat
# Jämför med dynamiskt typat och statiskt typat
antal_katter = 5
antal_hundar = "2"
#summa = antal_katter + antal_hundar #FUNKAR EJ


# Slå ihop strängar med + (konkatenera) och str()
syster_namn = "Frida"
sammanlagda_namn = namn  + syster_namn
#print(sammanlagda_namn)


### UTSKRIFTER ###

# Skriva ut flera saker på två sätt
#print("Hej", namn)
#print("Hej "+ namn)

# Skriva ut radbrytningar, citattecken och liknande
#print("\"\nHallå\tdär!")

# Skriva ut med formatering
#print(f"Hej där {namn} och {syster_namn}, hur mår ni idag?")

### INMATNINGAR ###

# input()
print("Vad är ditt intresse?")
intresse = input()

intresse_två = input("Vad är ditt andra intresse?")

print(f"Vad kul att du tycker om att {intresse} och {intresse_två}")


# Omvandla input till tal
antal_syskon = int(input("Hur många syskon har du? "))
print(antal_syskon+9)

