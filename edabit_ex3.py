import math


def line_length(dot1, dot2):
    cat1 = dot2[0] - dot1[0]
    cat2 = dot2[1] - dot1[1]

    hipotenusa = math.pow(cat1, 2) + math.pow(cat2, 2)
    length = math.sqrt(hipotenusa)
    print(round(length, 2))
    return round(length, 2)


line_length([15, 7], [22, 11])
