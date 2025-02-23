from pathlib import Path

path = Path("pi_digits.txt")

if path.exists():
    contents = path.read_text()
    contents = contents.rstrip()
    lines = contents.splitlines()
    pi_string = ""
    for line in lines:
        pi_string += line.lstrip()

    print(f"Pi value is {pi_string}")
else:
    print("Error: the file doesn't exists")

path_to_write = Path("programming.txt")
content_2 = "I love programming.\n"
content_2 += "I love creating new games.\n"
content_2 += "I also live working with dta.\n"
path_to_write.write_text(content_2)


def count_words(pathname):
    """Count the approximate number of words in a file."""
    try:
        path = Path(pathname)
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exists.")
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


count_words(pathname="words.txt")
