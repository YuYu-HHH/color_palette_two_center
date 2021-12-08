from Get_Palette_by_Two_center.Get_Tree_Root_New_Test import Get_Root_about_Tree
from Get_palettes.Get_Split_further import Broken_down_further_by_Color_Depth
import numpy as np

def Get_Tree_Root(result_palettes, result_weights, palette_rgb_five):
    colors = [];
    weights_new = [];

    for i in range(len(result_palettes)):
        result_palette = result_palettes[i];
        result_weight = result_weights[i];




        palettes1_one, palettes1_two, weights1_one, weights1_two, return1_num = Broken_down_further_by_Color_Depth(
            result_palette,result_weight);
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

    return colors,weights_new;