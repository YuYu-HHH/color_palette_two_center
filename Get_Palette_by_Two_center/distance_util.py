from colormath.color_conversions import convert_color
from colormath.color_objects import sRGBColor, HSVColor


def distance_num(num1,num2):
    n1 = num1[0];
    n2 = num1[1];
    n3 = num2[0];
    n4 = num2[1];
    return ((n1 - n3) ** 2 + (n2 - n4) ** 2) ** 0.5;


def distance_RGB_Hsv(rgb1,rgb2):
    RGB1 = sRGBColor(rgb1[0], rgb1[1], rgb1[2], is_upscaled=True)
    RGB2 = sRGBColor(rgb2[0], rgb2[1], rgb2[2], is_upscaled=True)
    hsv1 = convert_color(RGB1, HSVColor)
    hsv2 = convert_color(RGB2, HSVColor);
    # print(hsv1)

    H1 = hsv1.hsv_h;
    S1 = hsv1.hsv_s;
    V1 = hsv1.hsv_v;
    # print(H1);
    # print(S1);
    H2 = hsv2.hsv_h;
    S2 = hsv2.hsv_s;
    V2 = hsv2.hsv_v;



    return ((H1 - H2) ** 2 + (S1 - S2) ** 2) ** 0.5;