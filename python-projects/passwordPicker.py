import random
from string import punctuation


def select_noun() -> str:
    global nouns
    return random.choice(nouns)


def select_adjective() -> str:
    global adjectives
    return random.choice(adjectives)


def select_color() -> str:
    global colors
    return random.choice(colors)


def select_number() -> int:
    return random.randint(0, 100)


def select_punctuation() -> str:
    return random.choice(list(punctuation))


# Main
nouns = ['panda', 'potato', 'tomato', 'lion', 'pencake', 'dracon']
adjectives = ['pretty', 'ugly', 'beautiful', 'happy', 'naked']
colors = ['white', 'black', 'pink', 'blue', 'orange', 'green']


while 1:
    noun = select_noun()
    adjective = select_adjective()
    color = select_color()
    number = select_number()
    punctuation1 = select_punctuation()
    print('Your password is generated : ')
    print(color + adjective + noun + str(number) + punctuation1)
    other = input("Do you need another password y[Yes] , n[No]:").lower()
    if other == 'n' or other == 'No':
        print("Good bye!")
        break
