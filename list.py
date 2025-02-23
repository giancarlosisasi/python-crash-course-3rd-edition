# bycyles = ['trek', 'cannondable', 'redline', 'specialized']
# print(bycyles)
# del bycyles[0]
# print(bycyles)

# last_removed = bycyles.pop(0)
# print(bycyles)
# print(last_removed)

# bycyles.remove('trek')
# print(bycyles)

languages = ["c++", "rust", "go", "python", "javascript"]
print(languages)

languages[0] = "gleam"
print(languages)

languages.insert(0, "elixir")
languages.insert(3, "ocalm")
languages.append("r")
print(languages)

removed = languages.pop(0)
print(f"item removed was {removed}")
del languages[1]

print(languages)
languages.remove("gleam")
print(languages)

print(sorted(languages))
print(languages)
print(len(languages))

for lang in languages:
    print(f"I want to learn {lang}")

# def range(x, y=None):
#     if y is None:
#         return []

#     return []

for n in range(6):
    print(n)

squares = []

# for value in range(1, 11):
#     square = value ** 2
#     squares.append(square)
# print(squares)
squares = [value**2 for value in range(1, 11)]
print(squares)

player_scores = [1, 52, 15, 60, 21, 90]
print(player_scores)
best_three = sorted(player_scores)[-3:]

print(f"The best three scores are: {best_three}")

requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

for topping in requested_toppings:
    if topping == "green peppers":
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {topping}")
