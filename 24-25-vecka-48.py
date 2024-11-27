# Här är ett program som innehåller en del fel
# Vi ska åtgärda dem på följande sätt:
# 1. Se till att programmet går att köra
# 2. Testa funktionerna som ska finnas
# 3. Testa vad som händer om man skriver in konstiga saker och åtgärda det
# 4. Fundera om det är något mer vi kan göra för att öka användarvänligheten
import random

def generate_question(operation): 
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    if operation == "both":
        choice = random.randint(1,2)
        if choice == 1:
            operation = "multiply"
        else:
            operation = "divide"
    
    if operation == "multiply":
        question = "What is " + str(num1) + " * " + str(num2) + "? "
        answer = num1 * num2
    elif operation == "divide":
        question = "What is " + str(num1*num2) + "/" + str(num1) + "? "
        answer = num2
    


    return question, answer

def main():
    print("Welcome to the Math Quiz!")
    while True:
        operation = input("Choose an operation (multiply, divide, both, or quit to exit): ")
        if operation == "quit":
            print("Goodbye!")
            break
        num_questions = int(input("How many questions would you like to answer? "))
        score = 0
        for _ in range(num_questions):
            question, answer = generate_question(operation)
            user_answer = int(input(question))
            #user_answer = int(user_answer)
            if user_answer == answer:
                print("Correct!")
                score += 1
            else:
                print("Wrong! The correct answer is " + str(answer) + ".")
        print("You got " + str(score) + "out of " + str(num_questions) + " questions correct.")
        if num_questions > 0:
            percentage = (score / num_questions) * 100
            print("Your score: " + str(percentage) + "%")

main()