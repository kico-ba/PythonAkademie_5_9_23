"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Stefan Kicak
email: kico@kico.sk
discord: kico.mobil
"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

row = 40 * "-"
users = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"}
#print(users)
username = input("username:")
password = input("password:")
print(username,password)

if username in users and users[username] == password:
    print(row)
    print("Welcome to the app, " + username + "\n" + "We have 3 texts to be analyzed.")
    print(row)
else:
    print("unregistered user, terminating the program...")
    exit()

while True:
    text_number = (input("Enter a number btw. 1 and 3 to select: "))
    if text_number.isdigit():
        text_number = int(text_number)
        if 1 <= text_number <= 3:
            break
        else: print("Please enter a valid integer between 1 and 3.")
print(row)
print("You selected text number", text_number)
# print("First 30 char: " + selected_text[:30] + "...")
print(row)
selected_text = TEXTS[text_number -1]
selected_text_list = list(selected_text.split())
selected_string_list = list(selected_text)

# words
words = len(selected_text_list)
print("There are", words, "words in the selected text.")

# titlecase words
titlecase_words = 0
for word in selected_text_list:
    if word.istitle():
        titlecase_words += 1
print("There are", titlecase_words, "titlecase words.")        

# uppercase words
uppercase_words = 0
for word in selected_text_list:
    if word.isupper():
        uppercase_words += 1
print("There are", uppercase_words, "uppercase words.")  

# lowercase words
lowercase_words = 0
for word in selected_text_list:
    if word.islower():
        lowercase_words += 1
print("There are", lowercase_words, "lowercase words.")  

# numeric strings
numeric_strings = 0
for word in selected_text_list:
    if word.isnumeric():
        numeric_strings += 1
print("There are", numeric_strings, "numeric strings.") 

# Sum of all numbers
numbers = []
for number in selected_text_list:
    if number.isdigit():
        numbers.append(int(number))
print("The sum of all the numbers is:", sum(numbers))

print(row, "\n", "LEN|  OCCURENCES  |NR.", "\n", row)

# Differnet word lenght counts 
word_length_counts = {}
for word in selected_text_list:
    word_length = len(word)
    if word_length in word_length_counts:
        word_length_counts[word_length] += 1
    else:
        word_length_counts[word_length] = 1

sorted_lengths = sorted(word_length_counts.keys())

for length in sorted_lengths:
    count = word_length_counts[length]
    print(length, "|", ("*" * length), "|", count)
exit()