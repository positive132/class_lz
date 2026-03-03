import math

p = 3.14

length = float(input('Введите длину стороны октагона:'))

class Octagon: 
    def __init__(self, length:int):
        self._length = length
        self.k = 1 + 2 ** 0.5 
        self.ugle = 3 * p / 4 

def opis (length: float):

    R = length / 2 * (4 + 2 * (2) ** 0.5) ** 0.5
    area1 = p*(R) ** 2 

    return R, area1

def vpis (length: float):

    r = length/2 * (1 + (2) ** 0.5)
    area2 = p*(r)**2 

    return r, area2

def octagonperimpl(length: float):

    perimetr = 8 * length
    area3 = 2 * (1 + 2 ** 0.5) * (length ** 2)

    return perimetr, area3


def main():
    print('радиус и площадь описанной окружности:', opis(length))
    print('радиус и площадь вписанной окружности:', vpis(length))
    print('периметр и площадь октагона:', octagonperimpl(length)) 
    
if __name__ == '__main__':
    main()    