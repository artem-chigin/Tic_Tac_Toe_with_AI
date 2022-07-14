import random
import game_board


class EasyAi:
    def __init__(self, board, character):
        self.board = board
        self.character = character

    def ai_move(self):
        row = random.randint(0, 2)
        column = random.randint(0, 2)
        if game_board.cell_is_not_empty(self.board, row, column):
            return self.ai_move()
        else:
            self.board[row][column] = self.character
            return self.board


class MediumAi(EasyAi):
    def __init__(self, board, character, enemy_character):
        super().__init__(board, character)
        self.enemy_character = enemy_character

    def attack_two_from_three(self, board, mode):
        if mode == "A":
            if board.count(self.character) == 2 and board.count(" ") == 1:
                return board.index(" ")
        elif mode == "D":
            if board.count(self.enemy_character) == 2 and board.count(" ") == 1:
                return board.index(" ")

    def horizontal_move(self, b, mode):
        for row in range(len(b)):
            space_char_index = self.attack_two_from_three(b[row], mode)
            if space_char_index is not None:
                self.board[row][space_char_index] = self.character
                return self.board

    def vertical_move(self, b, mode):
        for row in range(len(b)):
            space_char_index = self.attack_two_from_three(b[row], mode)
            if space_char_index is not None:
                self.board[space_char_index][row] = self.character
                return self.board

    def main_diagonal_move(self, b, mode):
        main_diagonal_space_index = self.attack_two_from_three(b, mode)
        if main_diagonal_space_index is not None:
            self.board[main_diagonal_space_index][main_diagonal_space_index] = self.character
            return self.board

    def second_diagonal_move(self, b, mode):
        second_diagonal_space_field_index = self.attack_two_from_three(b, mode)
        if second_diagonal_space_field_index is not None:
            self.board[second_diagonal_space_field_index][len(b) - 1 - second_diagonal_space_field_index] = self.character
            return self.board

    def move(self, mode):
        board, rotated_board, main_diagonal, second_diagonal = game_board.parsing_board(self.board)

        move = self.horizontal_move(board, mode)
        if move is not None:
            return move
        move = self.vertical_move(rotated_board, mode)
        if move is not None:
            return move
        move = self.main_diagonal_move(main_diagonal, mode)
        if move is not None:
            return move
        move = self.second_diagonal_move(second_diagonal, mode)
        if move is not None:
            return move

    def medium_ai_move(self):

        result = self.move("A")
        if result is not None:
            return result
        result = self.move("D")
        if result is not None:
            return result

        return self.ai_move()
