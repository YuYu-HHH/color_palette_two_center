param_13 = 1.0 / 3.0
param_16116 = 16.0 / 116.0

Xn = 0.950456
Yn = 1.0
Zn = 1.088754


def RGB2XYZ(r, g, b):
    x = 0.412453 * r + 0.357580 * g + 0.180423 * b
    y = 0.212671 * r + 0.715160 * g + 0.072169 * b
    z = 0.019334 * r + 0.119193 * g + 0.950227 * b
    return x, y, z


def XYZ2Lab(x, y, z):
    x /= 255 * Xn
    y /= 255 * Yn
    z /= 255 * Zn
    if y > 0.008856:
        fy = pow(y, param_13)
        l = 116.0 * fy - 16.0
    else:
        fy = 7.787 * y + param_16116
        l = 903.3 * fy

    if l < 0:
        l = 0.0

    if x > 0.008856:
        fx = pow(x, param_13)
    else:
        fx = 7.787 * x + param_16116

    if z > 0.008856:
        fz = pow(z, param_13)
    else:
        fz = 7.787 * z + param_16116

    a = 500.0 * (fx - fy)
    b = 200.0 * (fy - fz)

    return [round(l, 2), round(a, 2), round(b, 2)]


def RGB2Lab(r, g, b):
    x, y, z = RGB2XYZ(r, g, b)
    return XYZ2Lab(x, y, z)