# Här är ett program som innehåller en del fel
# Vi ska åtgärda dem på följande sätt:
# 1. Se till att programmet går att köra
# 2. Testa funktionerna som ska finnas
# 3. Testa vad som händer om man skriver in konstiga saker och åtgärda det
# 4. Fundera om det är något mer vi kan göra för att öka användarvänligheten

# Problem:
# Om man säger att man vill ha tex -1 fråga
# Välja vilken tabell man ska lära
# Om man stavar fel på operation
# int runt saker kan ställa till problem

import random

def generate_question(operation): # Generearar fråga och svar utifrån vilken operation man väljer
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    if operation == "both": # Om man har valt both
        choice = random.randint(1,2) # Slumpar om det ska bli multiplikation eller division
        if choice == 1: # Om det blev multiplikation
            operation = "multiply"
        else: # Om det blev division
            operation = "divide"
    
    if operation == "multiply": # Om man valde eller det har slumpats till multiplikation
        question = "What is " + str(num1) + " * " + str(num2) + "? " # Frågan
        answer = num1 * num2 # Svaret
    elif operation == "divide": # Om man valde eller det ha slumpats till division
        question = "What is " + str(num1*num2) + "/" + str(num1) + "? " # Frågan
        answer = num2 # Svaret
    
    return question, answer # Ger tillbaka både frågan och svaret

def main():
    print("Welcome to the Math Quiz!")

    while True: # Så länge programmet ska köras
        operation = input("Choose an operation (multiply, divide, both, or quit to exit): ") # Fråga om operation
        if operation == "quit": # Om man valde quit
            print("Goodbye!")
            break # Bryt programmet
        
        while operation not in ["multiply", "divide", "both"]: # Sålänge användaren inte har skrivit in ett godkänt svar
            operation = input("Choose an operation (multiply, divide, both, or quit to exit): ") # Fråga igen

        
        try: # Testa följande
            num_questions = int(input("How many questions would you like to answer? ")) # Antal frågor, leder till ValueError om man skriver in annat än tal
            if num_questions <= 0: # Om man har svarat ett negativt tal
                raise ValueError # Då ska det också bli fel
            
            score = 0 # 0 poäng från början
            for _ in range(num_questions): # Loopa så många gånger som antalet frågor
                question, answer = generate_question(operation) # Får fråga och svar genom att kalla på funktionen generate_question
                not_right = True # Vi antar att användaren inte har svarat ett giltigt svar från början
                while not_right: # Så länge användaren inte har gett ett giltigt svar
                    try: # Testa följande
                        user_answer = int(input(question)) # Ta in användarens svar på frågan
                        if user_answer == answer: # Om svaret är rätt
                            print("Correct!")
                            score += 1 # Öka poängen
                        else: # Om svaret är fel
                            print("Wrong! The correct answer is " + str(answer) + ".")
                        not_right = False # Här har vi fått ett giltigt svar, då vill vi ur while-loopen
                    except ValueError: # Om svaret inte var ett heltal kommer while-loopen att fortsätta ställa samma fråga
                        print("Du behöver skriva in ett heltal")
            
            print("You got " + str(score) + " out of " + str(num_questions) + " questions correct.") # Sammanfattar resultat
            if num_questions > 0:
                percentage = (score / num_questions) * 100
                print("Your score: " + str(percentage) + "%") # Visar andelen rätt svar
        
        except ValueError: # Om det inte var ett heltal på antalet frågor kommer vi starta om programmet
            print("Du måste skriva in ett heltal som är större 0")

main()