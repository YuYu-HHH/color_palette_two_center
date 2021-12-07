import cv2
from PIL import Image
import numpy as np

from Get_Palette_by_Two_center.Two_Center_Al import two_center_Al, two_center
from Get_Palette_by_Two_center.distance_util import distance_num
from Get_Palette_by_Two_center.draw_figure import draw_figure, draw
from Get_Palette_by_Two_center.space_2_space import rgb_2_ab, rgb_2_lab, rgbs_2_abs, rgb_2_lab_l
from get_the_picture_about_color.extract_theme import extract_theme
from show import get_bigger_palette_to_show


def Get_Palette_by_Two_center(filename):
    I = np.asfarray(Image.open(filename).convert('RGB')) / 255.0
    k = 100;
    sigma = 40;
    discard_black = 1;
    palette, weights = extract_theme(I, k, sigma, discard_black);

    palette_rgb = np.array(palette);
    palette_img = get_bigger_palette_to_show(palette_rgb)
    # print(palette_img)
    Image.fromarray((palette_img).round().astype(np.uint8)).save("-convexhull_vertices.png");
    with open("colors_vertices.txt", 'a') as file_handle:
        file_handle.write(str(palette))
        file_handle.write('\n')
    with open("weights_new_vertices.txt", 'a') as file_handle:
        file_handle.write(str(weights))
        file_handle.write('\n')


    palette_ab = np.zeros([len(palette_rgb),2]);
    palette_lab = np.zeros([len(palette_rgb),3]);
    palette_l = np.zeros([len(palette_rgb),1]);
    for i in range(len(palette_rgb)):
        palette_ab[i] = rgb_2_ab(palette_rgb[i]);
        palette_lab[i] = rgb_2_lab(palette_rgb[i]);
        palette_l[i] = rgb_2_lab_l(palette_rgb[i]);


    #将palette按照L的大小分为  明暗  两部分。
    print(palette_l)
    palette_one = [];
    palette_two = [];
    palette_one_lab = [];
    palette_two_lab = [];
    palette_one_ab = [];
    palette_two_ab = [];
    for i in range(len(palette_rgb)):
        if palette_l[i] < 30:
            palette_one.append(palette_rgb[i])
            palette_one_lab.append(rgb_2_lab(palette_rgb[i]))
            palette_one_ab.append(rgb_2_ab(palette_rgb[i]));

        elif palette_l[i] > 30:
            palette_two.append(palette_rgb[i]);
            palette_two_lab.append(rgb_2_lab(palette_rgb[i]));
            palette_two_ab.append(rgb_2_ab(palette_rgb[i]));

    palette_one = np.array(palette_one);
    palette_img = get_bigger_palette_to_show(palette_one)
    Image.fromarray((palette_img).round().astype(np.uint8)).save("picture_one-palette_one.png");
    palette_two = np.array(palette_two)
    palette_img = get_bigger_palette_to_show(palette_two)
    Image.fromarray((palette_img).round().astype(np.uint8)).save("picture_one_palette_two.png");



    # draw_Color_Group(palette_ab);
    colors1 = two_center(palette_one);

    colors1 = np.array(colors1);

    colors2 = two_center(palette_two);
    colors2 = np.array(colors2);


    #去除 明亮中的黑暗的颜色 因为自己的代码中写的全局变量， 会一直添加，所以需要删除

    len_colors1 = len(colors1);

    for i in range(len_colors1):
        colors2 = np.delete(colors2,0,0);


    for i in range(len(colors1)):
        color = colors1[i];
        color = np.array(color)
        palettes_ab1 = rgbs_2_abs(color);
        draw(palettes_ab1,i,0);

        palette_img = get_bigger_palette_to_show(color)
        Image.fromarray((palette_img).round().astype(np.uint8)).save("picture_one_"+str(i)+"-vertices.png");

    for i in range(len(colors2)):
        color = colors2[i];
        color = np.array(color)
        color = np.array(color)
        palettes_ab1 = rgbs_2_abs(color);
        draw(palettes_ab1, i,1);
        palette_img = get_bigger_palette_to_show(color)
        Image.fromarray((palette_img).round().astype(np.uint8)).save("picture_two_" + str(i) + "-_vertices.png");

    weights_1 = [];
    weights_2 = [];
    for i in range(len(colors1)):
        colors = colors1[i];
        weight_1 = [];
        for j in range(len(colors)):
            color = colors[j];
            index = np.where(palette_rgb == color);
            weight_1.append(weights[index]);
        weights_1.append(weight_1);

    for i in range(len(colors2)):
        colors = colors1[i];
        weight_2 = [];
        for j in range(len(colors)):
            color = colors[j];
            index = np.where(palette_rgb == color);
            weight_2.append(weights[index]);
        weights_2.append(weight_2);

    





























def draw_Color_Group(palettes_ab):
    yes = 1;

    xy = np.zeros([len(palettes_ab),2]);
    xs = np.zeros([len(palettes_ab)]);
    ys = np.zeros([len(palettes_ab)]);
    radiuss = np.zeros(len(palettes_ab));

    palettes_ab = np.array(palettes_ab, np.float32);
    (x1, y1), radius = cv2.minEnclosingCircle(palettes_ab);

    # 画出来直观图
    draw_figure(palettes_ab, x1, y1, radius);


    #画出来直观图
    # draw_entire_figure(palettes_not_sorted_hsv,xs,ys,radiuss);
    # print(xy);
    # print(radiuss);
    yes = 1;
    return xy,yes;



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

    #画出来直观图
    # draw_entire_figure(palettes_not_sorted_hsv,xs,ys,radiuss);
    # print(xy);
    # print(radiuss);
    yes = 1;
    return xy1,xy2,yes;