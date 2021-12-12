import os

import cv2
from PIL import Image
import numpy as np

from Get_Palette_by_Two_center.Get_Tree_Root import Get_Tree_Root
from Get_Palette_by_Two_center.Get_Tree_Root_New_Test import Get_Tree_Roots
from Get_Palette_by_Two_center.Two_Center_Al import Colors
from Get_Palette_by_Two_center.distance_util import distance_num
from Get_Palette_by_Two_center.draw_figure import draw_figure, draw
from Get_Palette_by_Two_center.space_2_space import rgb_2_ab, rgb_2_lab, rgbs_2_abs, rgb_2_lab_l
from get_the_picture_about_color.extract_theme import extract_theme
from show import get_bigger_palette_to_show


def Get_Palette_by_Two_center(filename, save_Path):
    I = np.asfarray(Image.open(filename).convert('RGB')) / 255.0
    k = 100;
    sigma = 40;
    discard_black = 1;
    palette, weights = extract_theme(I, k, sigma, discard_black);

    palette_rgb = np.array(palette);
    palette_img = get_bigger_palette_to_show(palette_rgb)
    # print(palette_img)
    Image.fromarray((palette_img).round().astype(np.uint8)).save(save_Path + "\-convexhull_vertices.png");
    with open(save_Path + "\colors_vertices.txt", 'a') as file_handle:
        file_handle.write(str(palette))
        file_handle.write('\n')
    with open(save_Path + "\weights_new_vertices.txt", 'a') as file_handle:
        file_handle.write(str(weights))
        file_handle.write('\n')
    palette_ab = rgbs_2_abs(palette_rgb);
    draw(palette_ab,100,100,100,save_Path);
    for i in range(3):
        print("555555555555555555555555555555555555555555")
        print(len(palette_rgb))
        print(len(weights))
        palette_rgb, weights = Get_Palette_(palette_rgb,weights,save_Path, i);


def Get_Palette_(palette_rgb,weights,save_Path, t):
    palette_ab = np.zeros([len(palette_rgb), 2]);
    palette_lab = np.zeros([len(palette_rgb), 3]);
    palette_l = np.zeros([len(palette_rgb), 1]);
    for i in range(len(palette_rgb)):
        palette_ab[i] = rgb_2_ab(palette_rgb[i]);
        palette_lab[i] = rgb_2_lab(palette_rgb[i]);
        palette_l[i] = rgb_2_lab_l(palette_rgb[i]);

    # 将palette按照L的大小分为  明暗  两部分。

    palette_one = [];
    palette_two = [];
    palette_one_lab = [];
    palette_two_lab = [];
    palette_one_ab = [];
    palette_two_ab = [];
    for i in range(len(palette_rgb)):
        if palette_l[i] < 28:
            palette_one.append(palette_rgb[i])
            palette_one_lab.append(rgb_2_lab(palette_rgb[i]))
            palette_one_ab.append(rgb_2_ab(palette_rgb[i]));

        elif palette_l[i] > 28:
            palette_two.append(palette_rgb[i]);
            palette_two_lab.append(rgb_2_lab(palette_rgb[i]));
            palette_two_ab.append(rgb_2_ab(palette_rgb[i]));




    palette_one = np.array(palette_one);
    palette_img = get_bigger_palette_to_show(palette_one)
    Image.fromarray((palette_img).round().astype(np.uint8)).save(save_Path + "\picture_one-palette_one.png");
    palette_two = np.array(palette_two)
    palette_img = get_bigger_palette_to_show(palette_two)
    Image.fromarray((palette_img).round().astype(np.uint8)).save(save_Path + "\picture_one_palette_two.png");



    # draw_Color_Group(palette_ab);
    if len(palette_one) > 1:
        colorss = Colors();
        colors1 = colorss.two_center(palette_one);
    else:
        colors1 = palette_one;

    colors1 = np.array(colors1);
    colorss1 = Colors();
    colors2 = colorss1.two_center(palette_two);
    colors2 = np.array(colors2);

    # 去除 明亮中的黑暗的颜色 因为自己的代码中写的全局变量， 会一直添加，所以需要删除

    # len_colors1 = len(colors1);
    #
    # for i in range(len_colors1):
    #     colors2 = np.delete(colors2, 0, 0);
    if len(palette_one) >   1:
        for i in range(len(colors1)):
            color = colors1[i];
            color = np.array(color)
            palettes_ab1 = rgbs_2_abs(color);
            draw(palettes_ab1, i, 0,t,save_Path);
            palette_img = get_bigger_palette_to_show(color)
            save_Filename = os.path.join(save_Path,str(t)+"picture_one_" + str(i) + "-vertices.png")
            Image.fromarray((palette_img).round().astype(np.uint8)).save(save_Filename );
    elif len(palette_one) == 1:
        palettes_ab1 = rgbs_2_abs(colors1);
        draw(palettes_ab1, 0, 0, t, save_Path);
        palette_img = get_bigger_palette_to_show(colors1)
        save_Filename = os.path.join(save_Path, str(t) + "picture_one_" + str(0) + "-vertices.png")
        Image.fromarray((palette_img).round().astype(np.uint8)).save(save_Filename);

    for i in range(len(colors2)):
        color = colors2[i];
        color = np.array(color)
        color = np.array(color)
        palettes_ab1 = rgbs_2_abs(color);
        draw(palettes_ab1, i, 1,t,save_Path);
        palette_img = get_bigger_palette_to_show(color)
        save_Filename = os.path.join(save_Path, str(t) + "picture_two_" + str(i) + "-vertices.png");
        Image.fromarray((palette_img).round().astype(np.uint8)).save(save_Filename );

    weights_1 = [];
    weights_2 = [];
    if len(palette_one) > 1:
        for i in range(len(colors1)):
            colors = colors1[i];
            weight_1 = [];
            for j in range(len(colors)):
                color = colors[j];
                for k in range(len(palette_rgb)):
                    if all(palette_rgb[k] == color):
                        index = k;
                # print(index)
                weight_1.append(weights[index]);
            weights_1.append(weight_1);
    elif len(palette_one) == 1:
        weights_1 = weights_1;

    for i in range(len(colors2)):
        colors = colors2[i];
        weight_2 = [];
        for j in range(len(colors)):
            color = colors[j];
            for k in range(len(palette_rgb)):
                if all(palette_rgb[k] == color):
                    index = k;
            weight_2.append(weights[index]);
        weights_2.append(weight_2);

    len_index = len(colors1) + len(colors2);
    weights_max_index = np.argsort(-weights);
    weights_max_index_five = weights[weights_max_index];
    palette_rgb_five = palette_rgb[weights_max_index];
    palette_rgb_five = palette_rgb_five[0:len_index];

    colors1 = np.array(colors1);
    colors2 = np.array(colors2);
    if len(palette_one) > 1:
        colors_1, weights_new_1 = Get_Tree_Root(colors1, weights_1, palette_rgb_five);
    else:
        colors_1 = colors1;
        colors_1 = list(colors_1)
        weights_new_1 = weights_1;
    colors_2, weights_new_2 = Get_Tree_Root(colors2, weights_2, palette_rgb_five);

    colors1 = colors_1;
    colors2 = colors_2;
    weights_1 = weights_new_1;
    weights_2 = weights_new_2;

    colors_1.extend(colors_2);
    weights_new_1.extend(weights_new_2);
    colors = np.array(colors_1);
    weights_new_1 = np.array(weights_new_1);

    if len(palette_one) == 2:
        if distance_num(palette_one_ab[0],palette_one_ab[1]) < 40:
            color_an = (palette_one[0] + palette_one[1]) / 2;
            weight_an = (weights_1[0] + weights_1[1]);
             #删除前两个颜色 加入新的颜色
            for i in range(2):
                colors = np.delete(colors, 0, 0);
                weights_new_1 = np.delete(weights_new_1,0,0);
            colors = np.r_[colors, [color_an]];
            weights_new_1 = np.r_[weights_new_1,[weight_an]];


    print(len(colors));
    if t == 0:

        with open(save_Path + "\colors1.txt", 'a') as file_handle:
            file_handle.write(str(colors))
            file_handle.write('\n')
        with open(save_Path + "\weights_new1.txt", 'a') as file_handle:
            file_handle.write(str(weights_new_1))
            file_handle.write('\n')

        vertices_image = get_bigger_palette_to_show(colors);
        save_Filename = os.path.join(save_Path, "111weights-Split_not-vertices.png");
        Image.fromarray((vertices_image).round().astype(np.uint8)).save(
            save_Filename);
    if t == 1:
        with open(save_Path + "\colors2.txt", 'a') as file_handle:
            file_handle.write(str(colors))
            file_handle.write('\n')
        with open(save_Path + "\weights_new2.txt", 'a') as file_handle:
            file_handle.write(str(weights_new_1))
            file_handle.write('\n')

        vertices_image = get_bigger_palette_to_show(colors);
        save_Filename = os.path.join(save_Path, "222weights-Split_not-vertices.png");
        Image.fromarray((vertices_image).round().astype(np.uint8)).save(
            save_Filename);
    if t == 2:
        with open(save_Path +"\colors3.txt", 'a') as file_handle:
            file_handle.write(str(colors))
            file_handle.write('\n')
        with open(save_Path +"\weights_new3.txt", 'a') as file_handle:
            file_handle.write(str(weights_new_1))
            file_handle.write('\n')

        vertices_image = get_bigger_palette_to_show(colors);
        save_Filename = os.path.join(save_Path, "333weights-Split_not-vertices.png");
        Image.fromarray((vertices_image).round().astype(np.uint8)).save(
            save_Filename);
    if t == 3:
        with open(save_Path +"\colors4.txt", 'a') as file_handle:
            file_handle.write(str(colors))
            file_handle.write('\n')
        with open(save_Path +"\weights_new4.txt", 'a') as file_handle:
            file_handle.write(str(weights_new_1))
            file_handle.write('\n')

        vertices_image = get_bigger_palette_to_show(colors);
        save_Filename = os.path.join(save_Path, "444weights-Split_not-vertices.png");
        Image.fromarray((vertices_image).round().astype(np.uint8)).save(
            save_Filename);
    return colors,weights_new_1;





























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