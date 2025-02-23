player_scores = {"player_1": 25, "player_2": 30, "player_3": 50}

print(player_scores.get("player_1", "no value found"))

for key, value in player_scores.items():
    print(f"The player {key} has a score of {value}")

favorite_langues = {
    "jen": ["python", "rust"],
    "sarah": ["c"],
    "edward": ["rust", "go"],
    "phil": ["python", "haskell"],
}

for name, languages in favorite_langues.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
