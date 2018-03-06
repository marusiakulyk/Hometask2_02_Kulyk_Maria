import pprint
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
    list_of_coordinates = ((i, j) for j in range(10) for i in range(10))
    print(list_of_coordinates)
    lst = ['']
    list_around = ['']
    for ship in list_of_ships:
        while set(lst) & set(list_around):
            try:
                list_around = []
                a = random.choice(["horizontal", "vertical"])
                int_coord = random.choice(list(set(list_of_coordinates)-set(lst)))
                # int_coord[0] - row, int_coord[1] - column

                if a == "horizontal":
                    for i in range(int_coord[0] - 1, int_coord[0] + 2):
                        for j in range(int_coord[1] - 1, int_coord[1] + ship + 1):
                            list_around += (i, j)
                if a == "vertical":
                    for i in range(int_coord[0] - 1, int_coord[0] + ship + 1):
                        for j in range(int_coord[1] - 1, int_coord[1] + 2):
                            list_around += (i, j)

                if a == "horizontal":
                    for i in range(int_coord[0], int_coord[0] + ship):
                        field[i][int_coord[1]] = "*"

                if a == "vertical":
                    for i in range(int_coord[1], int_coord[1] + ship):
                        field[int_coord[0]][i] = "*"

                lst.extend(list_around)
            except IndexError:
                pass
                # list_around = ['']



#        coord_l, coord_num = ord(coord[0])-ord('a'), coord[1]-1
#        try:
#           if not has_ship(field, coord):
#                if a == "horizontal":
#                    lst1 = [coord1]
#                    for i in range(coord_l, coord_l+list_of_ships[k]):
#                        assert 0 <= i <= 9
#                        assert field[i][coord_num] == " "
#                        field[i][coord_num] = "*"
#                else:
#                    for i in range(coord_num, coord_num+list_of_ships[k]):
#                        assert 0 <= i <= 9
#                        assert field[coord_l][i] == " "
#                        field[coord_l][i] = "*"
#            else:
#                k -= 1
#        except AssertionError or IndexError:
#            k -= 1
    return field


def field_to_str(data):
    str1 = "  A B C D E F G H I J\n"
    for i, str2 in enumerate(data):
        str1 += '%+2s' % str(i+1) + " ".join(str2) + "\n"
    return str1


if __name__ == "__main__":
    a = read_data('file.txt')
    print(has_ship(a, ('a', 2)))
    print(ship_size(a, ('c', 1)))
    b = field_generate()
    print(field_to_str(b))
