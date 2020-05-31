from math import gcd
from functools import reduce
import itertools

text = input("Input text: ").upper()
min_letters = int(input("Mininum number of letters per duplicate group: "))
text_size = len(text)
duplicates = {}
unique_duplicates = {}
distances = []
ggt = 0
alfa = "abcdefghijklmnopqrstuvwxyz"
letters = []
sorted_letters = []
encrypted_sorted_letters = []
if " " in text:
    text = text.split(" ")
    text = "".join(text)

for start_letter in range(0, text_size + 1):
    for letter_index in range(start_letter, text_size - 1):
        if not letter_index - start_letter > min_letters - 2:
            continue
        substring = text[start_letter:letter_index + 1]
        if substring in text[letter_index:]:
            distance = text[letter_index + 1:].index(substring) + len(substring)
            print(distance + (len(substring)))
            # print(text[start_letter:])
            duplicates[substring] = distance
        else:
            break
        print(start_letter, substring)
        if letter_index - start_letter >= text_size / 2:
            break
for index, duplicate in enumerate(duplicates):
    unique = True
    for second_index, second_duplicate in enumerate(duplicates):
        if second_index == index:
            continue
        if duplicate in second_duplicate:
            unique = False
            break
    if unique:
        unique_duplicates[duplicate] = duplicates[duplicate]
        distances.append(duplicates[duplicate])

print(duplicates)
print(unique_duplicates)
ggt = reduce(gcd, distances)
print(ggt)

index_letters = {}
for i in range(0, ggt):
    index = i
    end = False
    while not end:
        if text[index] in index_letters:
            index_letters[text[index]] = index_letters[text[index]] + 1
        else:
            index_letters[text[index]] = 1
        index += ggt
        if index >= len(text):
            end = True
    letters.append(index_letters)
    index_letters = {}
for letter in letters:
    print(letter)
    sorted_letters.append(sorted(letter, key=letter.get, reverse=True)[:4])
    print("\n")
print(sorted_letters)

for letters in sorted_letters:
    encrypted_letters = []
    for letter in letters:
        letter_index = alfa.index(letter.lower())
        e_index = alfa.index("e")
        new_index = letter_index - e_index
        if new_index >= 0:
            encrypted_letters.append(alfa[new_index])
        else:
            encrypted_letters.append(alfa[len(alfa) + new_index])
    encrypted_sorted_letters.append(encrypted_letters)
print(encrypted_sorted_letters)

possibilities = list(itertools.product(*encrypted_sorted_letters))
for index,word in enumerate(possibilities):
    if index > 50:
        break
    print("".join(word))