#Sonni tubligini aniqlash dasturi
while True:
    tub=True

    n=int(input('Sonni kiriting'))

    for i in range(2,n):
         if n%i==0:
            tub=False

    if n==1:
        print(str(n) + '-Bu son tub emas')		
    elif n <= 0:
        print(str(n) + '-Bu son tub emas')
    elif tub:
        print(str(n) + '-Bu son tub')
    elif not tub:
        print(str(n) + '-Bu son tub emas')		
