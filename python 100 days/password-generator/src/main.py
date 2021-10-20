import random
import string
import time


def generatePassword(letter_count, symbol_count, number_count):
    letters = string.ascii_lowercase
    numbers = [str(i) for i in range(10)]
    symbols = string.punctuation
    random.seed(time.time())
    password = ''
    while letter_count != 0 or symbol_count != 0 or number_count != 0:
        arr = []
        if letter_count:
            arr = arr + list(letters)
        if number_count:
            arr = arr + numbers
        if symbol_count:
            arr = arr + list(symbols)
        choice = random.choice(arr)
        if choice in letters:
            letter_count -= 1
        if choice in numbers:
            number_count -= 1
        if choice in symbols:
            symbol_count -= 1
        password += choice
    return password


def main():
    print('Welcome to the PyPassword Generator')
    letter_count = int(input('How many letters would you like in your password?\n'))
    symbol_count = int(input('How many symbols would you like?\n'))
    number_count = int(input('How many numbers would you like?\n'))
    password = generatePassword(letter_count, symbol_count, number_count)
    print(f'Here is your password: {password}')


if __name__ == '__main__':
    main()
