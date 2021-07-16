def filter_list(lst):
    final_list = list()

    for elm in lst:
        if type(elm) == int:
            final_list.append(elm)
    return final_list


filter_list([1, 2, "aasf", "1", "123", 123])
