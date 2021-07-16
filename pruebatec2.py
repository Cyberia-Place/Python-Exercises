import random


def largest_sibling(n):
    family_list = list()
    bigger_num = 0
    while not len(family_list) == len(str(n)):
        input_n = list(str(n))
        number = ""
        print(input_n)

        while len(input_n) > len(family_list):
            random.shuffle(input_n)
            number = "".join(input_n)

            if not number in family_list:
                family_list.append(number)

    for number in family_list:
        if int(number) > bigger_num:
            bigger_num = int(number)

    print(bigger_num)
    return bigger_num


largest_sibling(5999)
