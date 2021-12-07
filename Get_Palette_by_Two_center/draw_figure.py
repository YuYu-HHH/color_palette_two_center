import matplotlib.pyplot as plt
import numpy as np
def draw_figure(palette_lab,x1,y1,radius):
    x = palette_lab[:,0];
    y = palette_lab[:,1];

    plt.figure(figsize=(10, 10), dpi=100)
    plt.scatter(x, y)
    a = np.arange(x1 - radius, x1 + radius, 0.001)
    b = np.sqrt(np.power(radius, 2) - np.power((a - x1), 2)) + y1
    plt.plot(a, b, color='r', linestyle='-')
    plt.plot(a, -b, color='r', linestyle='-')
    plt.scatter(0, 0, c='b', marker='o')
    plt.grid(True)
    plt.show();

def draw_entire_figure(palette_hsv,x1s,y1s,radiuss):
    x = palette_hsv[:,0];
    y = palette_hsv[:,1];
    plt.figure(figsize=(10, 10), dpi=100)
    plt.scatter(x, y)
    for i in range(len(x1s)):
        x1 = x1s[i];
        y1 = y1s[i];
        radius = radiuss[i];

        a = np.arange(x1 - radius, x1 + radius, 0.001)
        b = np.sqrt(np.power(radius, 2) - np.power((a - x1), 2)) + y1
        plt.plot(a, b, color='r', linestyle='-')
        plt.plot(a, -b, color='r', linestyle='-')

        plt.scatter(0, 0, c='b', marker='o')
        plt.grid(True)
    plt.show();