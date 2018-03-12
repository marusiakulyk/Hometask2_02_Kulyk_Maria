import string
import random


def read_data(filename):
    with open(filename) as f:
        lst = [list("{:<10}".format(line.strip('\n'))) for line in f]
    return lst


def has_ship(data, coord):
    return True if data[coord[1]-1][ord(coord[0])-ord('a')] == "*" else False


def ship_size(data, coord):
    if has_ship(data, coord):
        lst = [coord]
        for coord1 in lst:
            b = ord(coord1[0]) - ord('a')
            for i in range(coord[1]-1, coord[1]+2):
                for j in string.ascii_lowercase[b-1:b+2]:
                    if has_ship(data, (j, i)) and (j, i) not in lst:
                        lst.append((j, i))
        if lst[0][0] == lst[1][0]:
            return tuple([1, len(lst)])
        else:
            return tuple([len(lst), 1])


def is_valid(data):
    k = 0
    for i in data:
        for j in i:
            if j == "*":
                k += 1
    if k != 20:
        return False
    return True


def field_generate():
    list_of_ships = (4, 3, 3, 2, 2, 2, 1, 1, 1, 1)
    field = [[" " for i in range(10)]for j in range(10)]
    list_of_coordinates = [(i, j) for j in range(10) for i in range(10)]
    lst = ['']
    list_of_data = []
    for k in range(10):
        ship = list_of_ships[k]
        list_ship = ['']
        while True:
            try:
                list_around = []
                a = random.choice(["horizontal", "vertical"])
                int_coord = random.choice(list(set(list_of_coordinates) - set(lst)))
                coord = (chr(int_coord[1]+ord('a')),int_coord[0]+1)

                if a == "horizontal":
                    assert int_coord[1] + ship - 1 < 10
                    list_ship = [(int_coord[0], i) for i in range(int_coord[1], int_coord[1] + ship)]
                    assert not set(list_ship) & set(lst)
                    for i in range(int_coord[0] - 1, int_coord[0] + 2):
                        for j in range(int_coord[1] - 1, int_coord[1] + ship + 1):
                            list_around.append((i, j))

                if a == "vertical":
                    assert int_coord[0] + ship - 1 < 10
                    list_ship = [(i, int_coord[1]) for i in range(int_coord[0], int_coord[0] + ship)]
                    assert not set(list_ship) & set(lst)
                    for i in range(int_coord[0] - 1, int_coord[0] + ship + 1):
                        for j in range(int_coord[1] - 1, int_coord[1] + 2):
                            list_around.append((i, j))

                list_around = list(filter(lambda x: x[0] > -1 and x[1] > -1, list_around))

                for i in list_ship:
                    if i in lst:
                        continue
                    field[i[0]][i[1]] = "*"

                lst.extend(list_around)
                list_of_data.append((int_coord, a, list_of_ships[k]))
                break
            except (IndexError, AssertionError):
                continue
    return field, list_of_data


def field_to_str(data):
    str1 = "  A B C D E F G H I J\n"
    for i, str2 in enumerate(data):
        str1 += '%+2s' % str(i+1) + " ".join(str2) + "\n"
    return str1


field, list_of_data = field_generate()
print(field_to_str(field))
print(list_of_data)
