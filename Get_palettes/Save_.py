from PIL import Image
import numpy  as np

def save_pic(palette_rgb, standard_sorted_indices ,lex_sorted_indices):
    palettes_standard = palette_rgb[standard_sorted_indices];
    palette_img_standard = get_bigger_palette_to_show(palettes_standard)
    # print(palette_img_standard)
    Image.fromarray((palette_img_standard).round().astype(np.uint8)).save("-convexhull_vertices_standard.png");

    lex_sorted_indices_rgb = lex_sorted_indices['rgb'];
    palettes_rgb = palette_rgb[lex_sorted_indices_rgb];
    palette_img_rgb = get_bigger_palette_to_show(palettes_rgb)
    # print(lex_sorted_indices_rgb)
    Image.fromarray((palette_img_rgb ).round().astype(np.uint8)).save("-convexhull_vertices_rgb.png");

    lex_sorted_indices_hsv = lex_sorted_indices['hsv'];
    palettes_hsv = palette_rgb[lex_sorted_indices_hsv];
    palette_img_hsv = get_bigger_palette_to_show(palettes_hsv)
    # print(lex_sorted_indices_hsv)
    Image.fromarray((palette_img_hsv ).round().astype(np.uint8)).save("-convexhull_vertices_hsv.png");

    lex_sorted_indices_vhs = lex_sorted_indices['vhs'];
    palettes_vhs = palette_rgb[lex_sorted_indices_vhs];
    palette_img_vhs = get_bigger_palette_to_show(palettes_vhs)
    # print(lex_sorted_indices_vhs)
    Image.fromarray((palette_img_vhs ).round().astype(np.uint8)).save("-convexhull_vertices_vhs.png");

    lex_sorted_indices_lab = lex_sorted_indices['lab'];
    palettes_lab = palette_rgb[lex_sorted_indices_lab];
    palette_img_vhs = get_bigger_palette_to_show(palettes_lab)  ;
    # print(lex_sorted_indices_lab);

    Image.fromarray((palette_img_vhs ).round().astype(np.uint8)).save("-convexhull_vertices_lab.png");

def get_bigger_palette_to_show(palette):
    c = 50
    palette2 = np.ones((1 * c, len(palette) * c, 3))
    for i in range(len(palette)):
        palette2[:, i * c:i * c + c, :] = palette[i, :].reshape((1, 1, -1))
    return palette2