def getWinner(bids):
    win = bids[0]
    for i in range(len(bids)):
        if bids[i]['bid'] > win['bid']:
            win = bids[i]
    return win


def main():
    bids = []
    while 1:
        print('Is there has bid? (yes or no)')
        act = input()
        if act == 'no':
            break
        name = input('name: ')
        bid = int(input('bid: '))
        bids.append({'name': name, 'bid': bid})
    winner = getWinner(bids)
    print(f'Winner : {winner["name"]}, bid: {winner["bid"]}')


if __name__ == '__main__':
    print('Welcome to secret auction')
    main()
