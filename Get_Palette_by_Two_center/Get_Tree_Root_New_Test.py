from PIL import Image

from Get_palettes.Get_Split_further import Broken_down_further_Get_Two_center, Broken_down_further_by_Color_Depth
from Get_palettes.Get_Tree_root import Get_Tree_root
from Get_palettes.Save_ import get_bigger_palette_to_show
from Get_Palette_by_Two_center.space_2_space import rgbs_2_hsvs, rgb_2_hsv
from palette_sorter.color_palette import ColorPalette
from palette_sorter.comprehensive_single_palette_sorter import ComprehensiveSinglePaletteSorter
import numpy as np


def Get_Tree_Roots(result_palettes, result_weights, palette_rgb_five,k):
    colors = [];
    weights_new = [];
    for i in range(len(result_palettes)):

        result_palette = result_palettes[i];


        result_weight = result_weights[i];

        # vertices_image = get_bigger_palette_to_show(result_palette);
        # Image.fromarray((vertices_image).round().astype(np.uint8)).save(
        #     str(k) + "result_palette" + str(i) + "-vertices.png");

        if i == 0:
            color, weight_new_ = Get_Tree_root(result_palette, result_weight);
            colors.append(color);
            weights_new.append(weight_new_);
        else:
            palettes_new_one, palettes_new_two, weight_new_one, weight_new_two, return_base = Broken_down_further_Get_Two_center(
                result_palette, result_weight);
            palettes1_one, palettes1_two, weights1_one, weights1_two, return1_num = Broken_down_further_by_Color_Depth(
                palettes_new_one,weight_new_one);
            if return1_num == 1:
                colors1, weights_new1 = Get_Root_about_Tree(palettes1_one, weights1_one, palette_rgb_five);
                for i in range(len(colors1)):
                    colors.append(colors1[i]);
                    weights_new.append(weights_new1[i]);

                if len(palettes1_two) > 0:
                    palettes1_two = np.array(palettes1_two);
                    weights1_two = np.array(weights1_two);
                    colors2, weights_new2 = Get_Root_about_Tree(palettes1_two, weights1_two, palette_rgb_five);
                    for j in range(len(colors2)):
                        colors.append(colors2[j]);
                        weights_new.append(weights_new2[j]);
            else:
                colors1, weights_new1 = Get_Root_about_Tree(palettes_new_one, weight_new_one, palette_rgb_five);
                for i in range(len(colors1)):
                    colors.append(colors1[i]);
                    weights_new.append(weights_new1[i]);
            if len(palettes_new_two) > 0:
                palettes2_one, palettes2_two, weights2_one, weights2_two, return2_num = Broken_down_further_by_Color_Depth(
                    palettes_new_two, weight_new_two);
                if return2_num == 1:
                    palettes2_one = np.array(palettes2_one);
                    palettes2_two = np.array(palettes2_two);
                    weights2_one = np.array(weights2_one);
                    weights2_two = np.array(weights2_two);
                    colors1, weights_new1 = Get_Root_about_Tree(palettes2_one, weights2_one, palette_rgb_five);
                    for i in range(len(colors1)):
                        colors.append(colors1[i]);
                        weights_new.append(weights_new1[i]);
                    if len(palettes2_two) > 0:
                        colors2, weights_new2 = Get_Root_about_Tree(palettes2_two, weights2_two, palette_rgb_five);
                        for j in range(len(colors2)):
                            colors.append(colors2[j]);
                            weights_new.append(weights_new2[j]);
                else:
                    if len(palettes_new_two) > 0:
                        colors2, weights_new2 = Get_Root_about_Tree(palettes_new_two, weight_new_two, palette_rgb_five);
                        for j in range(len(colors2)):
                            colors.append(colors2[j]);
                            weights_new.append(weights_new2[j]);

            # vertices_image = get_bigger_palette_to_show(palettes_new_one);
            # Image.fromarray((vertices_image).round().astype(np.uint8)).save(
            #     "palettes_new_one" + str(i) + "_one-Split_Sorted-vertices.png");
            # if len(palettes_new_two) > 0:
            #     vertices_image_ = get_bigger_palette_to_show(palettes_new_two);
            #     Image.fromarray((vertices_image_).round().astype(np.uint8)).save(
            #         "palettes_new_two" + str(i) + "_two-Split_Sorted-vertices.png");


            # 排序
            # colors1, weights_new1 = Get_Root_about_Tree(palettes_new_one,weight_new_one,palette_rgb_five);
            # for i in range(len(colors1)):
            #     colors.append(colors1[i]);
            #     weights_new.append(weights_new1[i]);
            # if len(palettes_new_two) > 0:
            #     colors2, weights_new2 = Get_Root_about_Tree(palettes_new_two,weight_new_two,palette_rgb_five);
            #     for j in range(len(colors2)):
            #         colors.append(colors2[j]);
            #         weights_new.append(weights_new2[j])




    return colors, weights_new;




def Get_Tree_Roots1(result_palettes, result_weights, palette_rgb_five, len_index,k):
    colors = [];
    weights_new = [];
    for i in range(len_index):
        result_palette = result_palettes[i];
        result_weight = result_weights[i];
        result_palette_hsv = rgbs_2_hsvs(result_palette);

        vertices_image = get_bigger_palette_to_show(result_palette);
        Image.fromarray((vertices_image).round().astype(np.uint8)).save(
            str(k) + "result_palette" + str(i) + "-vertices.png");
        if i == 0:
            color, weight_new_ = Get_Tree_root(result_palette, result_weight);
            colors.append(color);
            weights_new.append(weight_new_);
        else:
            # palettes_new_one, palettes_new_two, weight_new_one, weight_new_two, return_base = Broken_down_further_Get_Two_center(
            #     result_palette, result_weight);
            palettes1_one, palettes1_two, weights1_one, weights1_two, return1_num = Broken_down_further_by_Color_Depth(
                result_palette,result_weight);
            palettes1_one = np.array(palettes1_one);
            palettes1_two = np.array(palettes1_two);
            weights1_one = np.array(weights1_one);
            weights1_two = np.array(weights1_two);
            if return1_num == 1:
                colors1, weights_new1 = Get_Root_about_Tree(palettes1_one, weights1_one, palette_rgb_five);
                for i in range(len(colors1)):
                    colors.append(colors1[i]);
                    weights_new.append(weights_new1[i]);

                if len(palettes1_two) > 0:
                    palettes1_two = np.array(palettes1_two);
                    weights1_two = np.array(weights1_two);
                    colors2, weights_new2 = Get_Root_about_Tree(palettes1_two, weights1_two, palette_rgb_five);
                    for j in range(len(colors2)):
                        colors.append(colors2[j]);
                        weights_new.append(weights_new2[j]);
            else:
                colors1, weights_new1 = Get_Root_about_Tree(result_palette, result_weight, palette_rgb_five);
                for i in range(len(colors1)):
                    colors.append(colors1[i]);
                    weights_new.append(weights_new1[i]);

            # vertices_image = get_bigger_palette_to_show(palettes_new_one);
            # Image.fromarray((vertices_image).round().astype(np.uint8)).save(
            #     "palettes_new_one" + str(i) + "_one-Split_Sorted-vertices.png");
            # if len(palettes_new_two) > 0:
            #     vertices_image_ = get_bigger_palette_to_show(palettes_new_two);
            #     Image.fromarray((vertices_image_).round().astype(np.uint8)).save(
            #         "palettes_new_two" + str(i) + "_two-Split_Sorted-vertices.png");


            # 排序
            # colors1, weights_new1 = Get_Root_about_Tree(palettes_new_one,weight_new_one,palette_rgb_five);
            # for i in range(len(colors1)):
            #     colors.append(colors1[i]);
            #     weights_new.append(weights_new1[i]);
            # if len(palettes_new_two) > 0:
            #     colors2, weights_new2 = Get_Root_about_Tree(palettes_new_two,weight_new_two,palette_rgb_five);
            #     for j in range(len(colors2)):
            #         colors.append(colors2[j]);
            #         weights_new.append(weights_new2[j])




    return colors, weights_new;













def Get_Tree_Roots_1(result_palettes, result_weights, palette_rgb_five, len_index, k):
    colors = [];
    weights_new = [];
    for i in range(len_index):
        result_palette = result_palettes[i];
        result_weight = result_weights[i];
        base_ = 0
        for j in range(len(result_palette)):

            if result_palette[j] in palette_rgb_five:
                base_ = 1;
                colors.append(result_palette[j]);
                weights_new.append(result_weight[j]);
        if base_ == 0:
            max_index = np.argmax(result_weight);
            colors.append(result_palette[max_index]);
            weights_new.append(np.sum(result_weight));
    return colors,weights_new




def Get_Root_about_Tree(palettes_new_one,weight_new_one,palette_rgb_five):
    colors = [];
    weights_new = [];
    yes = 0;
    for i in range(len(palettes_new_one)):
        if palettes_new_one[i]  in palette_rgb_five:
            yes = 1;
    if len(palettes_new_one) > 1:
        palettes_new_one_Color = ColorPalette(palettes_new_one);
        target_spaces = ['rgb', 'hsv', 'vhs', 'lab'];
        palettes_new_one_sorted = ComprehensiveSinglePaletteSorter(palettes_new_one_Color, target_spaces)
        standard_sorted_indices = palettes_new_one_sorted.standard_sort();
        print(palettes_new_one);
        palettes_new_one = np.array(palettes_new_one);
        weight_new_one = np.array(weight_new_one);
        palettes_sorted_one = palettes_new_one[standard_sorted_indices];
        weights_sorted_one = weight_new_one[standard_sorted_indices];

        for i in range(0, len(palettes_sorted_one) - 1, 2):
            palette_one = palettes_sorted_one[i];
            palette_two = palettes_sorted_one[i + 1];
            weight_one = weights_sorted_one[i];
            weight_two = weights_sorted_one[i + 1];
            if palette_one in palette_rgb_five and palette_two in palette_rgb_five:
                colors.append(palette_one);
                colors.append(palette_two);
                weights_new.append(weight_one);
                weights_new.append(weight_two);
            else:
                palettes = [];
                palettes.append(palette_one);
                palettes.append(palette_two);
                weights_ = [];
                weights_.append(weight_one);
                weights_.append(weight_two);
                palettes = np.array(palettes);
                weights_ = np.array(weights_);
                color, weights__ = Get_Tree_root(palettes, weights_);
                colors.append(color);
                weights_new.append(weights__);

    else:
        colors.append(palettes_new_one[0]);
        weights_new.append(weight_new_one[0]);
    return colors, weights_new;