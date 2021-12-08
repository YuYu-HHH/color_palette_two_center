import numpy as np
from colormath.color_conversions import convert_color
from colormath.color_objects import sRGBColor, HSVColor, LabColor


def rgbs_2_hss(rgbs):
    hsvs = np.zeros([len(rgbs),2]);
    for i in range(len(rgbs)):
        rgb = rgbs[i];
        hsv = rgb_2_hs(rgb);
        hsvs[i] = hsv;
    return hsvs;

def rgbs_2_hsvs(rgbs):
    hsvs = np.zeros([len(rgbs),3]);
    for i in range(len(rgbs)):
        rgb = rgbs[i];
        hsv = rgb_2_hsv(rgb);
        hsvs[i] = hsv;
    return hsvs;
def rgb_2_hs(rgb):
    print(rgb)
    RGB = sRGBColor(rgb[0], rgb[1], rgb[2], is_upscaled=True);
    HSV = convert_color(RGB, HSVColor);

    h = HSV.hsv_h;
    s = HSV.hsv_s;
    hs = [];
    hs.append(np.array([h,s]));
    return np.array(hs);
def rgb_2_hsv(rgb):
    RGB = sRGBColor(rgb[0], rgb[1], rgb[2], is_upscaled=True);
    HSV = convert_color(RGB, HSVColor);

    h = HSV.hsv_h;
    s = HSV.hsv_s;
    v = HSV.hsv_v;

    hs = [];
    hs.append(np.array([h,s,v]));
    return np.array(hs);















def rgb_2_ab(rgb):

    RGB = sRGBColor(rgb[0], rgb[1], rgb[2], is_upscaled=True);
    LAB = convert_color(RGB, LabColor);

    a = LAB.lab_a;
    b = LAB.lab_b;

    return np.array([a,b]);

def rgb_2_lab(rgb):
    RGB = sRGBColor(rgb[0], rgb[1], rgb[2], is_upscaled=True);
    LAB = convert_color(RGB, LabColor);

    l = LAB.lab_l;
    a = LAB.lab_a;
    b = LAB.lab_b;

    return np.array([l,a,b]);

def rgb_2_lab_l(rgb):
    RGB = sRGBColor(rgb[0], rgb[1], rgb[2], is_upscaled=True);
    LAB = convert_color(RGB, LabColor);

    l = LAB.lab_l;
    a = LAB.lab_a;
    b = LAB.lab_b;

    return l

def lab_2_rgb(lab):


    LAB = LabColor(lab[0],lab[1],lab[2]);
    RGB = convert_color(LAB, sRGBColor);

    r = RGB.rgb_r;
    g = RGB.rgb_g;
    b = RGB.rgb_b;

    return np.array([r,g,b]);


def rgbs_2_abs(rgbs):
    labs = np.zeros([len(rgbs),2]);
    for i in range(len(rgbs)):
        rgb = rgbs[i];
        RGB1 = sRGBColor(rgb[0], rgb[1], rgb[2], is_upscaled=True)
        lab1 = convert_color(RGB1, LabColor)
        # print(hsv1)

        A1 = lab1.lab_a;
        B1 = lab1.lab_b;

        labs[i] = np.array([A1,B1]);

    return labs;
def rgbs_2_labs(rgbs):
    labs = np.zeros([len(rgbs),2]);
    for i in range(len(rgbs)):
        rgb = rgbs[i];
        RGB1 = sRGBColor(rgb[0], rgb[1], rgb[2], is_upscaled=True)
        lab1 = convert_color(RGB1, LabColor)
        # print(hsv1)

        L1 = lab1.lab_l;
        A1 = lab1.lab_a;
        B1 = lab1.lab_b;

        labs[i] = np.array([L1,A1,B1]);

    return labs;
