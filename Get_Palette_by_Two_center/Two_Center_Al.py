import cv2

from Get_Palette_by_Two_center.distance_util import distance_num
import numpy as np

from Get_Palette_by_Two_center.draw_figure import draw_figure
from Get_Palette_by_Two_center.space_2_space import rgb_2_ab, rgbs_2_abs


def two_center_Al(palettes):



    pixels_one,pixels_two,pixels_one_ab,pixels_two_ab = Get_Two_Center(palettes);
    print(pixels_one_ab)
    print(pixels_two_ab)
    xy1,xy2,yes = Verify_color_group_by_distance_LAB(pixels_one_ab,pixels_two_ab);
    print(yes)

    colors = [];

    if yes == 0:
        yes1 = 0;
        yes2 = 0;
        if  yes1 == 0:

def one(pixels_one,pixels_two):
    Get_info(pixels_one);
    Get_info(pixels_two);

def Get_info(pixel):
    pixels_one, pixels_two, pixels_one_ab, pixels_two_ab = Get_Two_Center(pixel);
    xy1, xy2, yes1 = Verify_color_group_by_distance_LAB(pixels_one_ab, pixels_two_ab);
    return pixels_one, pixels_two;

def Get_Two_Center(palettes):
    dis_base = 0;
    index_base = np.zeros(2);
    # 1.先找出来两个距离最远的点
    for i in range(len(palettes)):
        for j in range(len(palettes)):
            # if i != j:
            #     dis = distance_num(rgb_2_ab(palettes[i]),rgb_2_ab(palettes[j]));
            #     if dis > dis_base:
            #         index_base = [i,j];
            #         dis_base = dis;
            dis = distance_num(rgb_2_ab(palettes[i]), rgb_2_ab(palettes[j]));

            if dis > dis_base:
                index_base = [i, j];
                dis_base = dis;
    # 2.分成两个中心

    center_two_one = palettes[index_base[0]];
    center_two_two = palettes[index_base[1]];

    center_two_one_ab = rgb_2_ab(center_two_one);
    center_two_two_ab = rgb_2_ab(center_two_two);

    labels = np.zeros([len(palettes)]);

    pixels_one_ab = [];
    pixels_two_ab = [];
    pixels_one = [];
    pixels_two = [];
    for i in range(len(palettes)):
        palette = palettes[i];
        palette_ab = rgb_2_ab(palette);

        dis_one = distance_num(palette_ab, center_two_one_ab);
        dis_two = distance_num(palette_ab, center_two_two_ab);

        if dis_one < dis_two:
            labels[i] = 0;
            pixels_one_ab.append(palette_ab);
            pixels_one.append(palette)
        else:
            labels[i] = 1;
            pixels_two_ab.append(palette_ab);
            pixels_two.append(palette)



    return pixels_one,pixels_two,pixels_one_ab,pixels_two_ab;

def Verify_color_group_by_distance_LAB(palettes_ab1,palettes_ab2):
    yes = 1;

    # xy1 = np.zeros([len(palettes_ab1),2]);
    # xs1 = np.zeros([len(palettes_ab1)]);
    # ys1 = np.zeros([len(palettes_ab1)]);
    # radiuss1 = np.zeros(len(palettes_ab1));

    palettes_ab1 = np.array(palettes_ab1, np.float32);
    (x1, y1), radius1 = cv2.minEnclosingCircle(palettes_ab1);
    xy1 = np.array([x1,y1])
    # 画出来直观图
    draw_figure(palettes_ab1, x1, y1, radius1);

    # xy2 = np.zeros([len(palettes_ab2), 2]);
    # xs2 = np.zeros([len(palettes_ab2)]);
    # ys2 = np.zeros([len(palettes_ab2)]);
    # radiuss2 = np.zeros(len(palettes_ab2));

    palettes_ab2 = np.array(palettes_ab2, np.float32);
    (x2, y2), radius2 = cv2.minEnclosingCircle(palettes_ab2);
    xy2 = np.array([x2, y2])

    # 画出来直观图
    draw_figure(palettes_ab2, x2, y2, radius2);


    if distance_num(xy1,xy2) < (radius1 + radius2 ):
        print("两个圆间距短，需要进一步分");
        yes = 0;
    else:
        print("两个圆间距长，不用分了")

    #画出来直观图
    # draw_entire_figure(palettes_not_sorted_hsv,xs,ys,radiuss);
    # print(xy);
    # print(radiuss);
    return xy1,xy2,yes;
