pets = ["cat", "dog", "parrot", "fish", "cat"]

while "cat" in pets:
    pets.remove("cat")

print("pets ", pets)

polling_active = True
responses = {}

while polling_active:
    name = input("what is your name?\n")
    response = input("Which mountain would you like to climb someday?\n")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (Yes/No)")

    if repeat == "No":
        polling_active = False

print("\n============== Poll results ============= \n")

for name, response in responses.items():
    print(f"{name} would like to climb {response}")
