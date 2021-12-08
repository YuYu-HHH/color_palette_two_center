import os

import cv2
import matplotlib.pyplot as plt
import numpy as np


def draw(palettes_ab1,i,k,t,save_Path):
    palettes_ab1 = np.array(palettes_ab1, np.float32);
    (x1, y1), radius1 = cv2.minEnclosingCircle(palettes_ab1);
    xy1 = np.array([x1, y1])
    # 画出来直观图
    draw_figure_save(palettes_ab1, x1, y1, radius1, i, k, t, save_Path);

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
    plt.grid(True);
    # plt.savefig(str(x1))
    plt.show();
def draw_figure_save(palette_lab,x1,y1,radius,i,k,t, save_Path):
    x = palette_lab[:,0];
    y = palette_lab[:,1];

    plt.figure(figsize=(10, 10), dpi=100)
    plt.scatter(x, y)
    a = np.arange(x1 - radius, x1 + radius, 0.001)
    b = np.sqrt(np.power(radius, 2) - np.power((a - x1), 2)) + y1
    plt.plot(a, b, color='r', linestyle='-')
    plt.plot(a, -b, color='r', linestyle='-')
    plt.scatter(0, 0, c='b', marker='o')
    plt.grid(True);
    one = os.path.join(save_Path,str(t) + "plot_picture_one_is"+str(i));
    two = os.path.join(save_Path, str(t) + "plot_picture_two_is" + str(i))
    if k == 0:plt.savefig(one);
    else:plt.savefig(two);

    # plt.show();
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

