import math
import random
class Player(object):
    def __init__(self, letter):
        self.__letter = letter

    def get_move(game):
        pass

class humanplayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(game):
        available_square = False
        value = None
        while not available_square:
            square = input(self.__letter + "\" s turn. Input move(0-8): ")
            try:
                value = int(square)
                if value not in game.moves_available():
                    raise ValueError
                available_square = True
            except ValueError:
                print("Invalid input pleaswe try again!")
        return value

class computerplayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(game):
        move = random.choice(game.moves_available)
        return move



