import cv2
from PIL import Image
import numpy as np

from Get_Palette_by_Two_center.Two_Center_Al import two_center_Al
from Get_Palette_by_Two_center.distance_util import distance_num
from Get_Palette_by_Two_center.draw_figure import draw_figure
from Get_Palette_by_Two_center.space_2_space import rgb_2_ab, rgb_2_lab, rgbs_2_abs
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
    for i in range(len(palette_rgb)):
        palette_ab[i] = rgb_2_ab(palette_rgb[i]);
        palette_lab[i] = rgb_2_lab(palette_rgb[i]);

    draw_Color_Group(palette_ab);

    two_center_Al(palette);












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