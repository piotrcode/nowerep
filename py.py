a = int(input('podaj pierwsza liczbe'))
b = int(input('podaj druga liczbe'))
def nwd(a, b):
if b > 0:
    return nwd(b, a%b)
else:
    return a
print('Patryk')