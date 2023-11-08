# Här är ett program som innehåller en del fel
# Vi ska åtgärda dem på följande sätt:
# 1. Se till att programmet går att köra
# 2. Testa funktionerna som ska finnas
# 3. Testa vad som händer om man skriver in konstiga saker och åtgärda det
# 4. Fundera om det är något mer vi kan göra för att öka användarvänligheten
import random

def generate_question(operation): # genrererar frågor, tar in en operation
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    if operation == "multiply": #om det är multiply
        question = "What is " + str(num1) + " * " + str(num2) + "? "
        answer = num1 * num2 # räknar ut svaret
    elif operation == "divide": # om det inte är multiply
        question = f"What is {num1*num2} / {num1} ? " # frågar om division
        answer = num2
    return question, answer # returnerar både frågan och svaret

def main(): # kör själva programmet
    print("Welcome to the Math Quiz!")
    while True:
        operation = input("Choose an operation (multiply, divide, or quit to exit): ")
        # Vill ha något som gör att frågan ställs igen om man skriver inte nonsens

        if operation == "quit": # om man vill avsluta programmet
            print("Goodbye!")
            break

        num_questions = int(input("How many questions would you like to answer? "))
        score = 0

        for _ in range(num_questions):
            question, answer = generate_question(operation)
            user_answer = input(question)

            user_answer = int(user_answer)

            if user_answer == answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is {answer}.")

        print(f"You got {score} out of {num_questions} questions correct.")
        if num_questions > 0:
            percentage = (score / num_questions) * 100
            print(f"Your score: {percentage}%")

main()