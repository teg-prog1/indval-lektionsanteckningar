# Listor, tuples, mängder, dictionarys

# Listor
# Kan lagra flera värden i en variabel

frukter = ["äpple","banan","mango","päron","mango"]

# Listor är ordnade, det vill säga ordningen spelar roll
# De är indexerade
#print(frukter[1])

# Listor går att förändra värdena på
frukter[2] = "granatäpple"
#print(frukter)

# Det kan finnas dubletter i listor

# Det går att spara olika datatyper i en lista
blandad_lista = ["Felicia", 24, 1.7, True]

# Vi kan loopa igenom en lista
#for element in blandad_lista:
 #   print(element)

# Vi kan plocka ut längden på en lista
#print(len(blandad_lista))

# Metoder för listor: https://www.w3schools.com/python/python_lists_methods.asp

# sort(), append(), pop(), remove(), reverse()

tal_lista = [1,6,4,8,2,5,7,3,2]
#print(tal_lista)
sorterad_lista = tal_lista.copy()
sorterad_lista.sort()
#print(tal_lista)
#print(sorterad_lista)

tal_lista.append(5)




#################################################################################################

# Tuples

bokstäver = ("a","o","u","å")

# Som listor, men de går inte att ändra

# Mer minneseffektiva och tidseffektiva

# Bättre att använda om man har värden som inte kommer att ändras

#################################################################################################

# Sets

matvaror = {"tacobröd","paprika","mjölk","paprika","paprika"}

# Ingen ordning, tillåter inte dubletter

print(matvaror)

# Går att lägga till och ta bort element, men inte byta ut eller ändra ett specifikt element

# metoder för sets: https://www.w3schools.com/python/python_sets_methods.asp

# issubset(), intersection(), difference()