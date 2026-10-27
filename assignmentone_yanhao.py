# ===== Task 2: QA Bot =====
def qa_bot():
    print("Question Answering Bot")
    question = input("Ask me something: ")

    if question == "hku":
        print("Bot: HKU is The University of Hong Kong.")
    elif question == "robot":
        print("Bot: A robot is a machine that can sense, think and act.")
    elif question == "jetson":
        print("Bot: Jetson Nano is an AI computer.")
    elif question == "ai":
        print("Bot: AI means Artificial Intelligence.")
    elif question == "human":
        print("Bot: Humans created robots and AI.")
    elif question == "hello":
        print("Bot: Hello! Nice to meet you.")
    elif question == "python":
        print("Bot: Python is a language.")
    elif question == "name":
        print("Bot: My name is Python Bot.")
    else:
        print("Bot: Sorry, I don't understand.")


# ===== Task 3: Calculator =====
def calculator():
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /): ")

    if op == "+":
        print("Result:", num1 + num2)
    elif op == "-":
        print("Result:", num1 - num2)
    elif op == "*":
        print("Result:", num1 * num2)
    elif op == "/":
        print("Result:", num1 / num2)
    else:
        print("Invalid operation")


# ===== Task Choose Menu =====
def main():
    while True:
        print("\n========== Assignment One ==========")
        print("1. Task 1: Turtle Drawing")
        print("2. Task 2: QA Bot")
        print("3. Task 3: Simple Calculator")
        print("0. Exit")
        choice = input("Please choose a task: ")

        if choice == "1":
            turtle_drawing()
        elif choice == "2":
            qa_bot()
        elif choice == "3":
            calculator()
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Please input the value in [0,1,2,3]")


main()