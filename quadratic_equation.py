import math


def get_roots(a, b, c):

    discriminant = b ** 2 - 4 * a * c
    if discriminant == 0:
        root1 = -b / (2 * a)
        return root1, None
    elif discriminant > 0:
        root1 = (-b - math.sqrt(discriminant)) / (2 * a)
        root2 = (-b + math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    else:
        return None, None
