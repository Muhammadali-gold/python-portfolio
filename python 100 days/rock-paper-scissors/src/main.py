import random
import time


def main():
    random.seed(time.time())
    rock = '''   
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''
    paper = '''    
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''
    scissors = '''    
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''
    elements = [rock, paper, scissors]
    print('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors')
    user_choice = input('')
    if user_choice not in ('0', '1', '2'):
        print('Choice is not valid')
        return
    else:
        user_choice = int(user_choice)
        print(elements[user_choice])
    print("Computer chose")
    computer_choice = random.randint(0, 2)
    print(elements[computer_choice])
    if user_choice == computer_choice:
        print('It\'s draw')
    if user_choice == 0:
        if computer_choice == 2:
            print('You win!')
        else:
            print('You lose!')
    elif user_choice == 1:
        if computer_choice == 0:
            print('You win!')
        else:
            print('You lose!')
    else:
        if computer_choice == 1:
            print('You win!')
        else:
            print('You lose!')


if __name__ == '__main__':
    main()
