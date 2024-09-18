
# Listor, tuples, mängder (set)

# Listor
# Kan lagra flera värden i en variabel

frukter = ["äpple", "päron", "banan"]
grönsaker = []

# Listor är ordnade, det vill säga ordningen spelar roll
# De är indexerade
print(frukter[1])


# Listor går att förändra värdena på
print(frukter)

frukter[1] = "mango"
print(frukter)

# Det kan finnas dubletter i listor
namn_elever = ["Rafael", "Victor", "Frida", "Frida"]


# Det går att spara olika datatyper i en lista
information = [8, 9.3, "hej", True]


# Vi kan loopa igenom en lista

for element in information:
    print(element)

# Vi kan plocka ut längden på en lista
    
print(len(information))


# Metoder för listor: https://www.w3schools.com/python/python_lists_methods.asp

# sort(), append()
grönsaker.append("gurka")
grönsaker.append("paprika")
grönsaker.append("morot")
grönsaker.append("tomat")
print(grönsaker)

grönsaker.sort()
print(grönsaker)

#################################################################################################
# printa variabler i strings

tal = 8
tal2 = 7

print("Ditt resultat är: "+str(tal))
print("Ditt resultat är:",tal)
print(f"Ditt resultat är: {tal+tal2}")


#################################################################################################

# Tuples
vokaler = ("a","o","u","å")


# Som listor, men de går inte att ändra

# Mer minneseffektiva och tidseffektiva

# Bättre att använda om man har värden som inte kommer att ändras

#################################################################################################

# Sets


# Ingen ordning, tillåter inte dubletter

namn = {"Elias","Elicia","Zoe","Elias","Elicia","Elicia","Josefin"}
print(namn)


# Går att lägga till och ta bort element, men inte byta ut eller ändra ett specifikt element

namn.add("Minna")
namn.remove("Zoe")

# metoder för sets: https://www.w3schools.com/python/python_sets_methods.asp

# issubset()

x = {"a", "b", "c","t"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)


