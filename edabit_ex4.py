def construct_deconstruct(s):
    output_list = list()
    count = 0
    i = 0
    while count + 1 <= len(s)*2 - 1:
        if count + 1 > len(s):
            output_list.append(s[0: i - 1])
            i -= 1
            count += 1
        else:
            output_list.append(s[0:i + 1])
            i += 1
            count += 1
    print(output_list)
    return output_list


construct_deconstruct("Hello")
