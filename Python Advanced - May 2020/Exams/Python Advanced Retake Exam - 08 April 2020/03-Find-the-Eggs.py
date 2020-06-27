def find_strongest_eggs(arg, sub_lists):
    sub_list = [arg[i::sub_lists] for i in range(sub_lists)]
    strongest_egg = []

    for i in sub_list:
        middle_inx = int(len(i) / 2)
        left = i[middle_inx - 1]
        middle = i[middle_inx]
        right = i[middle_inx + 1]

        if right < middle > left:
            if right > left:
                strongest_egg.append(middle)

    return strongest_egg