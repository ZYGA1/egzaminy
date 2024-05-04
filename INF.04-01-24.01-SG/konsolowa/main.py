arr = input("podaj pesel: ")
if len(arr) != 11:
    arr = input("podaj poprawnyn pesel: ")
def sol(arr):
    S = 0
    waga = [1,3,7,9,1,3,7,9,1,3]
    for i in range(len(arr) - 1):
        S += int(arr[i]) * waga[i]
    M = S % 10
    if M ==0:
        R = 0
    else:
        R = 10 - M
    if R == int(arr[-1]):
        return True
    return False
def plec(arr):
    if int(arr[10]) % 2 == 0:
        return 'M' 
    else:
        return 'F'

print(f'{sol(arr)}, {plec(arr)}')
