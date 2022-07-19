import random
import math
import game_board


class EasyAi:
    def __init__(self, board, character):
        self.board = board
        self.character = character

    def easy_ai_move(self):
        row = random.randint(0, 2)
        column = random.randint(0, 2)
        if game_board.cell_is_not_empty(self.board, row, column):
            return self.easy_ai_move()
        else:
            self.board[row][column] = self.character
            return self.board


class MediumAi(EasyAi):
    def __init__(self, board, character, enemy_character):
        super().__init__(board, character)
        self.enemy_character = enemy_character

    def two_from_three_check(self, board, mode):
        if mode == "A":
            if board.count(self.character) == 2 and board.count(" ") == 1:
                return board.index(" ")
        elif mode == "D":
            if board.count(self.enemy_character) == 2 and board.count(" ") == 1:
                return board.index(" ")

    def horizontal_move(self, b, mode):
        for row in range(len(b)):
            space_char_index = self.two_from_three_check(b[row], mode)
            if space_char_index is not None:
                self.board[row][space_char_index] = self.character
                return self.board

    def vertical_move(self, b, mode):
        for row in range(len(b)):
            space_char_index = self.two_from_three_check(b[row], mode)
            if space_char_index is not None:
                self.board[space_char_index][row] = self.character
                return self.board

    def main_diagonal_move(self, b, mode):
        main_diagonal_space_index = self.two_from_three_check(b, mode)
        if main_diagonal_space_index is not None:
            self.board[main_diagonal_space_index][main_diagonal_space_index] = self.character
            return self.board

    def second_diagonal_move(self, b, mode):
        second_diagonal_space_field_index = self.two_from_three_check(b, mode)
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

        return self.easy_ai_move()


class HardAi(MediumAi):

    def hard_ai_move(self):
        move = None
        best_score = - math.inf
        virtual_board = self.board.copy()
        for row in range(3):
            for column in range(3):
                if virtual_board[row][column] == " ":
                    virtual_board[row][column] = self.character
                    score = self.minmax(virtual_board, False)
                    virtual_board[row][column] = " "
                    if score > best_score:
                        best_score = score
                        move = (row, column)
        row, column = move
        self.board[row][column] = self.character
        return self.board

    def minmax(self, board, is_ai_turn):
        if game_board.game_state(board) == "X wins" and self.character == "X" \
                or game_board.game_state(board) == "O wins" and self.character == "O":
            return 100
        if game_board.game_state(board) == "X wins" and self.character == "O" \
            or game_board.game_state(board) == "O wins" and self.character == "X":
            return - 100
        if game_board.game_state(board) == "Draw":
            return 0

        if is_ai_turn:
            best_score = - math.inf
            for row in range(len(board)):
                for column in range(len(board)):
                    if board[row][column] == " ":
                        board[row][column] = self.character
                        score = self.minmax(board, False)
                        board[row][column] = " "
                        best_score = max(best_score, score)
        else:
            best_score = math.inf
            for row in range(len(board)):
                for column in range(len(board)):
                    if board[row][column] == " ":
                        board[row][column] = self.enemy_character
                        score = self.minmax(board, True)
                        board[row][column] = " "
                        best_score = min(best_score, score)
        return best_score

