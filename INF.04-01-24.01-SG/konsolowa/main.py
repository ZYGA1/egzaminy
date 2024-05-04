
class Pesel:

    def __init__(self, pesel):
        self.s = pesel
    
    def getInf(self):
        print(f'{self.sol(self.s)}, {self.plec(self.s)}')

    def sol(self, arr):
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
    def plec(self, arr):
        if int(arr[10]) % 2 == 0:
            return 'M' 
        else:
            return 'F'


if __name__ ==  '__main__':
    pesel = Pesel('55030101193')
    pesel.getInf()
    

