import functions


class Ship:
    def __init__(self, bow, horizontal, length):
        self.bow = bow
        self.horizontal = horizontal
        self.length = length
        self.hit = [(i, j, False) for j in range(self.bow[1], self.bow[1]+self.length[1])
                    for i in range(self.bow[0], self.bow[0]+self.length[0])]

    def shoot_at(self, tuple_):
        tuple1 = tuple_ + (False,)
        for i, tuple2 in enumerate(self.hit):
            if tuple2 == tuple1:
                self.hit[i] = tuple_ + (True,)


class Field:

    def __init__(self):
        self.__ships = [[None for i in range(10)]for j in range(10)]
        self.field, field_data = functions.field_generate()
        for ship in field_data:
            ship1 = Ship(ship[0], ship[1], ship[2])
            for coord in ship1.hit:
                self.__ships[coord[0]][coord[1]] = ship1

    def shoot_at(self, tuple1):
        a = self.__ships[tuple1[0]][tuple1[1]]
        if self.__ships[tuple1[0]][tuple1[1]] is None:
            self.__ships[tuple1[0]][tuple1[1]] = "shooted"
        elif type(self.__ships[tuple1[0]][tuple1[1]]) == Ship:
            Ship.shoot_at(self.__ships[tuple1[0]][tuple1[1]], tuple1)
            for i in self.__ships[tuple1[0]][tuple1[1]].hit:
                if i[2] == False:
                    break
            else:
                for i in range(a.bow[0] - 1, a.bow[0] + a.length[0] + 1):
                    for j in range(a.bow[1] - 1, a.bow[1] + a.length[1] + 1):
                        if (i, j, True) not in a.hit and (0 <= i <= 10) \
                                and (0 <= j <= 10):
                            self.__ships[i][j] = "shooted"


    def field_without_ships(self):
        str1 = "   A B C D E F G H I J\n"
        for i, data in enumerate(self.__ships):
            str1 += '%+2s' % str(i+1)
            for j, sym in enumerate(data):
                if sym == "shooted":
                    a = '*'
                elif type(sym) == Ship and (i, j, True) in sym.hit:
                    a = "x"
                else:
                    a = " "
                str1 += " " + a
            str1 += '\n'
        return str1

    def field_with_ships(self):
        return self.__ships


class Player:
    def __init__(self, name):
        self.__name = name

    def read_position(self):
        x = str(input("Player {}, enter move"
                      .format(self.__name)).lower())
        x2 = ord(x[0]) - ord('a')
        x1 = int(x[1:])-1
        return tuple([x1, x2])


last_iterat = 0


class Game:
    def __init__(self, fields, players):
        global last_iterat
        last_iterat += 1
        self.fields = fields
        self.players = players
        self.iterat = last_iterat
        self.current_player = self.players[self.iterat % 2]

    def read_position(self):
        return self.current_player.read_position()

    def field_without_ships(self, index):
        a = self.fields[index-1].field_without_ships()
        return a

    def field_with_ships(self, index):
        return self.fields[index-1].field_with_ships()


field1 = Field()
field2 = Field()
player1 = Player(1)
player2 = Player(2)
game = Game([field1, field2], [player1, player2])
print(functions.field_to_str(field1.field))
print(functions.field_to_str(field2.field))
while True:
    for i in range(2):
        a = game.players[i].read_position()
        game.fields[i-1].shoot_at(a)
        print(game.field_without_ships(i))
