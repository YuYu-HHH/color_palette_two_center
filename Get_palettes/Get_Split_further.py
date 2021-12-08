import cv2

from Get_Palette_by_Two_center.distance_util import distance_num
from Get_Palette_by_Two_center.space_2_space import rgbs_2_hss, rgbs_2_hsvs, rgbs_2_abs, rgb_2_lab
import numpy as np

from Get_Palette_by_Two_center import draw_figure


def Broken_down_further_Get_Two_center(result_palette,result_weight):
    return_base = 0;
    palettes_not_sorted_hsv = rgbs_2_hss(result_palette);
    palettes_not_sorted_hsv_x = palettes_not_sorted_hsv[:,0];
    dis_sum = 0
    for i in range(len(palettes_not_sorted_hsv)):
        for j in range(len(palettes_not_sorted_hsv)):
            if i != j:
                dis = abs(palettes_not_sorted_hsv_x[i] - palettes_not_sorted_hsv_x[j]);
                dis_sum = dis + dis_sum;
    dis_sum = dis_sum / 2;

    dis_base = dis_sum / len(palettes_not_sorted_hsv_x);

    palettes_not_sorted_hsv_x_index = np.argsort(palettes_not_sorted_hsv_x);
    palettes_not_sorted_hsv_x_sort = palettes_not_sorted_hsv_x[palettes_not_sorted_hsv_x_index];

    index_Split = 0;
    for i in range(len(palettes_not_sorted_hsv_x)-1):
        dis = abs(palettes_not_sorted_hsv_x_sort[i] - palettes_not_sorted_hsv_x_sort[i+1]);
        # print(dis)
        if dis > 10:
            return_base = 1;
            index_Split = i;
    palettes_new_one = [];
    palettes_new_two = [];

    weight_new_one = [];
    weight_new_two = [];
    index_Split = index_Split + 1;

    if index_Split != 0:
        index_Split = index_Split
        for j in range(index_Split):
            palettes_new_one.append(result_palette[palettes_not_sorted_hsv_x_index[j]]);
            weight_new_one.append(result_weight[palettes_not_sorted_hsv_x_index[j]]);
        for j in range(index_Split,len(palettes_not_sorted_hsv)):
            palettes_new_two.append(result_palette[palettes_not_sorted_hsv_x_index[j]]);
            weight_new_two.append(result_weight[palettes_not_sorted_hsv_x_index[j]]);

    palettes_new_one = np.array(palettes_new_one);
    palettes_new_two = np.array(palettes_new_two);


    weight_new_one = np.array(weight_new_one);
    weight_new_two = np.array(weight_new_two);
    return palettes_new_one, palettes_new_two, weight_new_one, weight_new_two, return_base;

def Broken_down_further_by_Color_Depth(palettes,weights):
    hsvs = rgbs_2_hsvs(palettes);
    hsvs_v = hsvs[:,2];
    hsv_sort_index = np.argsort(hsvs_v);
    hsv_max_index = np.argmax(hsvs_v);
    hsv_min_index = np.argmin(hsvs_v);

    hsv_max = hsvs[hsv_max_index];
    hsv_min = hsvs[hsv_min_index];

    sum = np.sum(hsvs_v);
    num = sum / len(palettes);
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(num)
    indexs = [];
    for i in range(len(palettes)):
        v = hsvs_v[i];
        if v < 0.35:
            indexs.append(i);
    # for i in range(len(palettes)):
    #     v = hsvs_v[i];
    #     if v < num:
    #         indexs.append(i);
    return_num = 0;
    palettes_one = [];
    palettes_two = [];
    weights_one = [];
    weights_two = [];
    if len(indexs) != 0:
        return_num = 1;
        for i in range(len(palettes)):
            if i in indexs:
                palettes_one.append(palettes[i]);
                weights_one.append(weights[i]);
            else:
                palettes_two.append(palettes[i]);
                weights_two.append(weights[i]);
    return palettes_one, palettes_two, weights_one, weights_two, return_num;

def Broken_down_further_by_Color_Depth_LAB(palettes,weights):
    hsvs = rgbs_2_hsvs(palettes);
    hsvs_v = hsvs[:,2];
    hsv_sort_index = np.argsort(hsvs_v);
    hsv_max_index = np.argmax(hsvs_v);
    hsv_min_index = np.argmin(hsvs_v);

    hsv_max = hsvs[hsv_max_index];
    hsv_min = hsvs[hsv_min_index];

    indexs = [];
    for i in range(len(palettes)):
        v = hsvs_v[i];
        if v < 0.4:
            indexs.append(i);

    return_num = 0;
    palettes_one = [];
    palettes_two = [];
    weights_one = [];
    weights_two = [];
    if len(indexs) != 0:
        return_num = 1;
        for i in range(len(palettes)):
            if i in indexs:
                palettes_one.append(palettes[i]);
                weights_one.append(weights[i]);
            else:
                palettes_two.append(palettes[i]);
                weights_two.append(weights[i]);
    return palettes_one, palettes_two, weights_one, weights_two, return_num;

#判断分类之后的 组之前的距离
#用来判断是否可以停止分类
# def Verify_color_group_distance(palettes,palettes_not_sorted):
#     yes = 1;
#
#     xy = np.zeros([len(palettes),2]);
#     xs = np.zeros([len(palettes)]);
#     ys = np.zeros([len(palettes)]);
#     radiuss = np.zeros(len(palettes));
#     for i in range(len(palettes)):
#         palette = palettes[i];
#         palette_hsv = rgbs_2_hsvs(palette);
#         palette_hsv = np.array(palette_hsv,np.float32);
#         (x1, y1), radius = cv2.minEnclosingCircle(palette_hsv);
#         xy[i] = [x1,y1];
#         radiuss[i] = radius;
#         #画出来直观图
#         # draw_figure(palette_hsv, x1, y1, radius);
#         xs[i] = x1;
#         ys[i] = y1;
#     for i in range(len(palettes)):
#         xy_i = xy[i];
#         for j in range(len(palettes)):
#             xy_j = xy[j];
#             dis = distance_num(xy_i,xy_j);
#             if dis < radiuss[i] and dis < radiuss[j]:
#                 print("group and group is :",i,"and ",j);
#                 yes = 0;
#     #画出来直观图
#     # draw_entire_figure(palettes_not_sorted_hsv,xs,ys,radiuss);
#     # print(xy);
#     # print(radiuss);
#     return xy,yes;


def Verify_color_group_distance_LAB(palettes,palettes_not_sorted):
    yes = 1;

    xy = np.zeros([len(palettes),2]);
    xs = np.zeros([len(palettes)]);
    ys = np.zeros([len(palettes)]);
    radiuss = np.zeros(len(palettes));
    palettes_not_sorted_hsv = rgbs_2_hsvs(palettes_not_sorted)
    for i in range(len(palettes)):
        palette = palettes[i];
        palette_lab = rgb_2_lab(palette);
        palette_lab = np.array(palette_lab,np.float32);
        (x1, y1), radius = cv2.minEnclosingCircle(palette_lab);
        xy[i] = [x1,y1];
        radiuss[i] = radius;
        #画出来直观图
        draw_figure(palette_lab, x1, y1, radius);
        xs[i] = x1;
        ys[i] = y1;
    for i in range(len(palettes)):
        xy_i = xy[i];
        for j in range(len(palettes)):
            xy_j = xy[j];
            dis = distance_num(xy_i,xy_j);
            if dis < radiuss[i] and dis < radiuss[j]:
                print("group and group is :",i,"and ",j);
                yes = 0;
    #画出来直观图
    # draw_entire_figure(palettes_not_sorted_hsv,xs,ys,radiuss);
    # print(xy);
    # print(radiuss);
    yes = 1;
    return xy,yes;