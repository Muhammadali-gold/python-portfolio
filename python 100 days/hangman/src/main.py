import random
import time

logo = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
# You guessed a, that's not in the word. You lose a life.
phases = [
    '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
]


def getSecretWord():
    words = ['Age', 'appear', 'artist', 'autumn', 'Bay', 'beak', 'bloom', 'bumpy', 'burst', 'buzz', 'Care', 'check',
             'chilly', 'chore', 'comfort', 'community', 'country', 'covered', 'cradle', 'Dangle', 'decision',
             'delicious', 'dentist', 'dew', 'disappear', 'drawer', 'dusty', 'Edge', 'Farmer', 'fear', 'firefly', 'fix',
             'flipper', 'fluffy', 'follow', 'Gallop', 'gentle', 'giggle', 'glance', 'glossy', 'glow', 'goal', 'gust',
             'Half', 'healthy', 'herd', 'hoof', 'Include', 'invitation', 'Knight', 'Laundry', 'lazy', 'leaf', 'leak',
             'library', 'Market', 'melt', 'miserable', 'month', 'muddy', 'museum', 'Note', 'Pace', 'pair', 'patient',
             'peaceful', 'peck', 'pilot', 'plan', 'pointy', 'polite', 'pond', 'president', 'protect', 'proud', 'Race',
             'reach', 'relax', 'rotten', 'round', 'row', 'Sail', 'scene', 'scrub', 'shade', 'shaky', 'ship', 'shore',
             'silky', 'sink', 'slide', 'slip', 'sniff', 'soapy', 'sparkle', 'spotted', 'spring', 'stare', 'summer',
             'supplies', 'Tangled', 'tent', 'tomorrow', 'trade', 'trunk', 'Warm', 'wave', 'week', 'wiggle', 'winter',
             'wish', 'Yesterday', 'young']
    random.seed(time.time())
    return random.choice(words)


def guessed(blank, guess, secret_word):
    g = False
    for i, a in enumerate(secret_word):
        if a == guess:
            blank[i] = a
            g = True
    return g


def main():
    secret_word = getSecretWord().lower()
    stage = 0
    print(logo)
    blank = ['_' for _ in secret_word]
    guess_history = []
    while 1:
        guess = input('Guess a letter: ').lower()
        if guess in guess_history:
            print(f'You guessed {guess} in previous attempts. Please another guess')
            continue
        guess_history.append(guess)
        if guessed(blank, guess,secret_word):
            print('')
        else:
            print(phases[stage])
            print(f'You guessed {guess}, that\'s not in the word. You lose a life.')
            stage += 1
        if stage == 6:
            print("You lose! Game over.")
            return
        if '_' not in blank:
            print(blank)
            print('You win!')
            return
        print(blank)


if __name__ == '__main__':
    main()
