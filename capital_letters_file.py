capital_letters = []
file_name = 'demo.txt'
with open(file_name) as countletter:
    text = countletter.read()
    for character in text:
        if character.isupper():
            capital_letters.append(character)

number_of_capital_letters = len(capital_letters)
print(number_of_capital_letters)