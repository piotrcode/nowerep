x = int(input('Podaj liczbe byczq: '))

for i in range(0, x+1):
    if i%2 == 0 and i%3 != 0:
        print(i)