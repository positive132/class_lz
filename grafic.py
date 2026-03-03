import matplotlib.pyplot as plt
import numpy as np
import lz_1

length = lz_1.length
p = lz_1.p

def main():
    def graf(length, p):

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

    graf(length, p)

if __name__ == '__main__':
    main()    