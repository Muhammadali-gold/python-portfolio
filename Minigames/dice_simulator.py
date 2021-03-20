import random
import time
random.seed(int(time.time()))
def dice():
    n=random.randint(1,6)
    dice_surfaces=[
        '''
    ┌────────────┐
    │            │
    │            │
    │     *      │
    │            │
    │            │
    └────────────┘
        ''',
        '''
    ┌────────────┐
    │            │
    │       *    │
    │            │
    │   *        │
    │            │
    └────────────┘
        ''',
        '''
    ┌────────────┐
    │            │
    │  *         │
    │     *      │
    │        *   │
    │            │
    └────────────┘
        ''',
        '''
    ┌────────────┐
    │            │
    │   *    *   │
    │            │
    │   *    *   │
    │            │
    └────────────┘
        ''',
        '''
    ┌────────────┐
    │            │
    │  *       * │
    │      *     │
    │  *       * │
    │            │
    └────────────┘
        ''',
        '''
    ┌────────────┐
    │            │
    │  *      *  │
    │  *      *  │
    │  *      *  │
    │            │
    └────────────┘
        ''',
    ]
    print(dice_surfaces[n-1])

def play():
    while 1:
        cmd=input("Throw cube (y,n)?")
        if cmd.lower()=='yes' or cmd.lower()=='y':
            dice()
        else:
            break

if __name__ == '__main__':
    play()