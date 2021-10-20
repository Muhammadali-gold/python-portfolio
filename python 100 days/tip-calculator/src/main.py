if __name__ == '__main__':
    print('Welcome to the tip calculator ')
    total_bill=float(input('What was the total bill? '))
    person_count=int(input('How may people split bill? '))
    percent=int(input('What percentage tip would you like to give? 10, 12, or 15? '))
    print(f'Each person should pay ${round(total_bill*(100+percent)/100/person_count,2)}')