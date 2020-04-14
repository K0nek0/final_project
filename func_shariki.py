import numpy as np
import matplotlib.pyplot as plt

R = 2
N = 20
v = 1
x0 = 0
y0 = 0

def func(R, N, v, x0, y0):
    coordinate = np.ndarray(shape=(N,2))
    velocity = np.ndarray(shape=(N,2))
    alpha = 2*np.pi/N

    for i in range(N):
        x = R * np.cos(i * alpha)
        y = R * np.sin(i * alpha)

        coordinate[i][0] = x+x0
        coordinate[i][1] = y+y0

        if x<0 and y<0:
            vx = v*np.sin(alpha*i)
            vy = -v*np.cos(alpha*i)

        elif x<0 and y>0:
            vx = v*np.sin(alpha*i)
            vy = -v*np.cos(alpha*i)

        elif x>0 and y>0:
            vx = v*np.sin(alpha*i)
            vy = -v*np.cos(alpha*i)

        elif x>0 and y<0:
            vx = v*np.sin(alpha*i)
            vy = -v*np.cos(alpha*i)

        else:
            vx = 0
            vy = -v*np.cos(alpha*i)

        velocity[i][0] = vx
        velocity[i][1] = vy

        plt.plot(coordinate[i][0], coordinate[i][1], marker = 'o')
        plt.plot(x0, y0, marker = 'o')
        plt.arrow(coordinate[i][0], coordinate[i][1], velocity[i][0], velocity[i][1])

        plt.axis('equal')

    plt.show()

    return coordinate, velocity

c, v = func(R, N, v, x0, y0)
