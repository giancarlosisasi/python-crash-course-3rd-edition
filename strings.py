name = "ada lovelace"

print(name.title())
print(name.lower())
print(name.upper())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
message_2 = f"hello, {full_name.title()}!"
print(message_2)

favorite_language = 'python           '
favorite_language_2 = favorite_language.rstrip()
print(favorite_language)
print(favorite_language_2)

nostarch_url = 'https://nostarch.com'
print(nostarch_url)
nostarch_url = nostarch_url.removeprefix('https://')
print(nostarch_url)

file_name_with_ext = "python.py"
file_name = file_name_with_ext.removesuffix(".py")
print(file_name)
