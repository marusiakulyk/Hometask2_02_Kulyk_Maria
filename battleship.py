import functions


class Game:
    iterat = 0

    def __init__(self, field, players):
        self.__field = field
        self.__players = players
        self.iterat += 1
        self.__current_player = self.__players[self.iterat % 2]

    def shoot_at(self, index, tuple1):
        pass

    def field_without_ships(self, index):
        pass

    def field_with_ships(self, index):
        return functions.field_to_str(self.__field[index-1]._Field__ships)


class Player:
    def __init__(self, name):
        self.__name = name

    def read_position(self):
        x = tuple(input("Player {}, enter move"
                           .format(self.__name)).lower())
        return x


class Field:
    def __init__(self):
        self.__ships = functions.field_generate()

    def shoot_at(self, tuple1):
        pass

    def field_without_ships(self):
        pass

    def with_ships(self):
        return self.__ships


class Ship:
    def __init__(self, bow, horizontal, length, hit):
        pass

    def shoot_at(self):
        pass


field1 = Field()
field2 = Field()
player1 = Player(1)
player2 = Player(2)
game = Game([field1, field2], [player1, player2])
print(game.field_with_ships(1))
while True:
    for i in range(2):
        a = game._Game__players[i].read_position()
        print(game._Game__fields[i].field_without_ships())
