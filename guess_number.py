import random

guess_number = random.randint(1, 10)

prompt = """
Welcome to the 'Guest Number' Game!
To start, please tell me your name: """

username = input(prompt)
guess = 0

print(f"Welcome {username}\n")

while guess != guess_number:
    guess = input("What is the number you think I'm thinking? ")
    guess = int(guess)
    if guess == guess_number:
        print("Nice! you win!")
    else:
        print("Ups! Not this time. Try again.\n")
