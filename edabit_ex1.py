def find_odd(lst):
    i = 0
    while i + 1 <= len(lst):
        count = 0
        num = lst[i]
        # Hasta aca funciona
        for elm in lst:
            if elm == num:
                # print(elm, num)
                count += 1
        # print(count - int(count))
        count = count/2
        if not (count - int(count) == 0):
            print(count/2, num, type(count/2))
            return num
        i += 1


find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5])
