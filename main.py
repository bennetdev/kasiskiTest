#Imports
from math import gcd
from functools import reduce
import itertools

#Get encrypted Text and convert to upper
text = input("Input text: ").upper()
min_letters = int(input("Mininum number of letters per duplicate group: "))
#initialise other variables
text_size = len(text)
duplicates = {}
unique_duplicates = {}
distances = []
ggt = 0
alfa = "abcdefghijklmnopqrstuvwxyz"
letters = []
sorted_letters = []
encrypted_sorted_letters = []
#remove whitespace in text
if " " in text:
    text = text.split(" ")
    text = "".join(text)
#iterate in range of text_size
for start_letter in range(0, text_size + 1):
    #iterate in range of following indices of current letter
    for letter_index in range(start_letter, text_size - 1):
        #check length of current substring
        if not letter_index - start_letter > min_letters - 2:
            continue
        #convert indices to substring
        substring = text[start_letter:letter_index + 1]
        #check if substring(current word group) is reoccuring
        if substring in text[letter_index:]:
            #get distance between this and next occurance
            distance = text[letter_index + 1:].index(substring) + len(substring)
            print(distance + (len(substring)))
            #add to duplicates dictionary
            duplicates[substring] = distance
        #else dont do anything
        else:
            break
        print(start_letter, substring)
        #stop loop after going trough half of the text
        if letter_index - start_letter >= text_size / 2:
            break
#Filter equal duplicates
#iterate over the duplicates
for index, duplicate in enumerate(duplicates):
    unique = True
    #iterate over duplicates
    for second_index, second_duplicate in enumerate(duplicates):
        if second_index == index:
            continue
        #if duplicate is reoccuring in duplicates
        if duplicate in second_duplicate:
            # set unique to false
            unique = False
            break
    if unique:
        #save duplicate
        unique_duplicates[duplicate] = duplicates[duplicate]
        #save duplicate distance
        distances.append(duplicates[duplicate])

print(duplicates)
print(unique_duplicates)
# get the ggt (len of password)
ggt = reduce(gcd, distances)
print(ggt)

index_letters = {}
#iterate over range of ggt
for i in range(0, ggt):
    index = i
    end = False
    while not end:
        # add to counter if letter in index_letters
        if text[index] in index_letters:
            index_letters[text[index]] = index_letters[text[index]] + 1
        # set counter to 1
        else:
            index_letters[text[index]] = 1
        # jump to next ggt index
        index += ggt
        # break on end
        if index >= len(text):
            end = True
    #append index_letters to overall letters
    letters.append(index_letters)
    #reset index_letters
    index_letters = {}
for letter in letters:
    print(letter)
    #sort letters
    sorted_letters.append(sorted(letter, key=letter.get, reverse=True)[:4])
    print("\n")
print(sorted_letters)
#iterate over the sorted_letters
for letters in sorted_letters:
    encrypted_letters = []
    #iterate over current array letters
    for letter in letters:
        #get alphabet index if current letter
        letter_index = alfa.index(letter.lower())
        #get index of e
        e_index = alfa.index("e")
        #see offset between current letter and letter e
        new_index = letter_index - e_index
        if new_index >= 0:
            #that is the index of the letter the letter was encrypted with
            encrypted_letters.append(alfa[new_index])
        else:
            #reverse the index
            encrypted_letters.append(alfa[len(alfa) + new_index])
    encrypted_sorted_letters.append(encrypted_letters)
print(encrypted_sorted_letters)
#create all combinations of passwords (most likely ones first)
possibilities = list(itertools.product(*encrypted_sorted_letters))
#print first 50
for index,word in enumerate(possibilities):
    if index > 50:
        break
    print("".join(word))