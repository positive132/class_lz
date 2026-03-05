import math
import matplotlib.pyplot as plt
import numpy as np

p = 3.14
length = float(input('Введите длину стороны октагона:'))

class Octagon: 
    def __init__(self, length: float):
        self.length = length
        self.k = 1 + 2 ** 0.5 
        self.ugle = 3 * p / 4 

    def opis (self):

        R = self.length / 2 * (4 + 2 * (2) ** 0.5) ** 0.5
        area1 = p*(R) ** 2 

        return R, area1

    def vpis (self):

        r = self.length / 2 * (1 + (2) ** 0.5)
        area2 = p*(r)**2 

        return r, area2

    def perimpl(self):

        perimetr = 8 * self.length
        area3 = 2 * (1 + 2 ** 0.5) * (self.length ** 2)

        return perimetr, area3
    def graf(self):

        R = length / 2 * (4 + 2 * (2) ** 0.5) ** 0.5
        ugles = np.linspace(0, 2 * p, 9) + p / 8
        r = length / 2 * (1 + (2) ** 0.5)
        circle_ugles = np.linspace(0, 2 * p, 100)

        x = R * np.cos(ugles)
        y = R * np.sin(ugles)

        plt.figure(figsize=(5, 5))

        plt.plot(R * np.cos(circle_ugles), R * np.sin(circle_ugles),'y', lw = 2.5)
        
        plt.plot(r * np.cos(circle_ugles), r * np.sin(circle_ugles),'r', lw = 2.5)
        plt.plot(x, y, 'b-o', lw = 2.5) 

        plt.show()

def main():
    octagon = Octagon(length)
    print('радиус и площадь описанной окружности:',octagon.opis() )
    print('радиус и площадь вписанной окружности:',octagon.vpis())
    print('периметр и площадь октагона:', octagon.perimpl()) 
    octagon.graf()
    
if __name__ == '__main__':
    main()    
