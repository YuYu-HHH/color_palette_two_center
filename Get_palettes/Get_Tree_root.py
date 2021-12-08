#2021.11.23 实验使用权重来对颜色进行重新计算
import numpy as np

from Get_Palette_by_Two_center.distance_util import distance_RGB_Hsv
from Get_Palette_by_Two_center.space_2_space import rgb_2_ab, rgb_2_lab, lab_2_rgb


def Get_Tree_root(palettes,weights):

    # if len(palettes) == 1:
    #     return palettes[0],weights[0];
    # else:
    #     weights_sum = np.sum(weights);
    #     weights_ = weights / weights_sum;
    #     color = np.zeros(3);
    #     # palette_sum = np.zeros(3);
    #     for i in range(len(weights)):
    #         palette = palettes[i];
    #         # palette = palette * weights_[i];
    #         palette_lab = rgb_2_lab11(palette)
    #         color = color + palette_lab;
    #     # print("--------------------")
    #     # print(color)
    #     color = color / len(weights);
    #     color = lab_2_rgb(color);
    #     return color,weights_sum;


    if len(palettes) == 1:
        return palettes[0],weights[0];
    else:
        weights_sum = np.sum(weights);
        # weights_ = weights / weights_sum;
        color = np.zeros(3);
        # palette_sum = np.zeros(3);
        for i in range(len(weights)):
            palette = palettes[i];
            palette = palette * weights[i];
            color = color + palette;
        # print("--------------------")
        # print(color)
        color = color / weights_sum;
        return color,weights_sum;





def Get_Tree_roots(palettes,weights,palettes_rgb_five):

    if len(palettes) == 1:
        return palettes,weights;
    else:
        #都是主要色，返回
        minest = np.min(weights);
        if minest > 10000:
            return palettes,weights;
        else:
            num, centers = num_max_(palettes,palettes_rgb_five);
            if num == 1:
                color, weights_ = cal_new_color(palettes , weights);
                color = color.reshape([1,3]);
                weights_ = [weights_];
            elif num == 0:
                color, weights_ = cal_new_color(palettes, weights);
                color = color.reshape([1, 3]);
                weights_ = [weights_];
            else:
                color,weights_ = cal_color_by_centers(palettes,centers,weights);
            color = np.array(color);
            weights_ = np.array(weights_);
            return color,weights_;

def cal_color_by_centers(palettes,centers,weights):
    label = np.zeros(len(palettes));

    for i in range(len(palettes)):
        palette = palettes[i];
        dis_base = 100000;
        for j in range(len(centers)):
            center = centers[j];
            dis = distance_RGB_Hsv(palette,center);
            if dis < dis_base:
                dis_base = dis;
                label[i] = j;
    uniques = np.unique(label);

    for i in range(len(centers)):
        centers_element = [];
        weights_element = [];
        for j in range(len(label)):
            if label[j] == i:
                centers_element.append(palettes[j]);
                weights_element.append(weights[j]);
        center_,weight_ = cal_new_color(centers_element,weights_element);
        centers[i] = center_;
        weights[i] = weight_;
    return centers,weights;


def get_center(center_element,weights):
    weight = 0;
    center = np.zeros(3);
    for i in range(len(weights)):
        weight = weights[i] + weight;
    for i in range(len(center_element)):
        center_element = center + center_element;
    return center , weight;

def cal_new_color(palettes, weights):

    weights_sum = np.sum(weights);
    weights_ = weights / weights_sum;
    color = np.zeros(3);
    for i in range(len(weights)):
        palette = palettes[i];
        palette = palette * weights_[i];
        color = color + palette;
    color = np.array(color);
    weights_sum = np.array(weights_sum);
    return color, weights_sum;


def num_max_(palettes,palettes_rgb_five):
    num = 0;
    palettes_ = [];
    for i in range(len(palettes)):
        palette = palettes[i]
        for j in range(len(palettes_rgb_five)):
            palette_rgb_five = palettes_rgb_five[j];
            if all(palette == palette_rgb_five):
                num = num + 1;
                palettes_.append(palette);
    palettes_ = np.array(palettes_);
    return num , palettes_;
