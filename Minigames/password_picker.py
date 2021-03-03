import random 
import string

adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fat']

nouns = ['apple', 'dinosaur', 'ball', 'panda']

print ('Welcome to Password Picker')
while True:

    for num in range(3):
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        number = random.randrange(0, 100)
        special_char = random.choice(string.punctuation)
    
        password = adjective + noun + str(number) + special_char
        print('Your new password is ' + password)

    response = input('Would you like another password? Tyoe y or n: ')
    if response == 'n':
        break
