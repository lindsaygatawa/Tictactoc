from Player import humanplayer
from Player import computerplayer
class tictactoe:

    def __init__(self):
        self.__board = [" " for i in range(9)]
        self.__currentwinner = None

    def printboard(self):
        for row in [self.__board[i*3:(i+1)*3] for i in range(3)]:
            print(" | " + " | " .join(row) + " | ")

    @staticmethod
    def print_board_numbers():
        """tells us what number corresponds to which box on the board"""
        number = [[str(i) for i in range(j*3, (j+1) *3)] for j in range(3)]
        for row in number:
            print(" | " + " | " .join(row) + " | ")
    """to know which spaces are not occupied"""
    def moves_available(self):
        moves = []
        for (i, spot) in enumerate(self.__board):
            if spot == " ":
                moves.append(i)
        return moves

    """Checks if there are any empty spaces on the board"""
    def empty_squares(self):
        return " " in self.__board

    """tells number of empty squares"""
    def num_empty_spaces(self):
        return len(self.moves_available())

    """function to get our move"""
    def make_move(self, square, letter):
        if self.__board[square] == " ":
            self.__board[square] = letter
            if self.winner(square, letter):
                self.__currentwinner = letter
            return True
        return False

    """To check if the letters are 3 in a row"""
    def winner(self, square, letter):
        row_ind = square // 3
        row = self.__board[row_ind*3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        """Check column"""
        col_ind = square % 3
        column = [self.__board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        """Check diagonals"""
        if square % 2 == 0:
            diagonal1 = [self.__board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.__board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_numbers()
    """While game still has empty squares continue iterating"""
    letter = "X"
    while game.empty_sqaures():
        if letter == "o":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f"makes a move to square {square}")
                game.printboard()
                print(" ")

            """Now we need to alternate letters"""
            letter = "o" if letter == "X" else "X"
            if letter == "X":
                letter = "o"
            else:
                letter = "X"
if __name__== "__main__ ":
   x_player = humanplayer("X")
   o_player = computerplayer("o")
   t = tictactoe()
   play(t, x_player, o_player, print_game=True)
