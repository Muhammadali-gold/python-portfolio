import string


def caeser_cipher(word, shift, action):
    word_list = list(word)
    abc = list(string.ascii_lowercase)
    if action == 'encode':
        for i, c in enumerate(word_list):
            if c in abc:
                word_list[i] = abc[(abc.index(c) + shift) % len(abc)]
    if action == 'decode':
        for i, c in enumerate(word_list):
            if c in abc:
                word_list[i] = abc[(abc.index(c) - shift) % len(abc)]
    return ''.join(word_list)


def main():
    action = input('You want encode or decode:\n').lower()
    word = input('Type word:\n').lower()
    shift = int(input('Type number for shift:\n'))
    ciphered = caeser_cipher(word, shift, action)
    print(f'{action}d word: {ciphered}')
    if input('If you want use again app , type \'yes\' or type \'no\'!:\n') == 'yes':
        main()


if __name__ == '__main__':
    print('Welcome to Caeser cipher.')
    main()
    print('Goodbye')
