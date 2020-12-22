m = int(input('podaj pierwsza liczbe'))
n = int(input('podaj druga liczbe'))
def nwd(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
print(nwd(m, n))