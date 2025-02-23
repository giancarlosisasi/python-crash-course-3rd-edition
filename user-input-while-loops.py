prompt = """
Hi there!
Please tell me your name!: """
name = input(prompt)

print(f"Hello {name}!")

age = input("\nNow, can you tell me what is your age? ")

age = int(age)

print(f"Oh wow! You are {age} years old!\n")


print("Starting while loop!\n")

state = "active"
message = ""
prompt_2 = """
Tell me something and I'll repeat it back to you:
Enter 'quit' to end the program.
"""
while state != "exiting":
    message = input(prompt_2)
    if message == "quit":
        state = "exiting"
    else:
        print(message)
