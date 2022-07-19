import ai_player
import game_board


def game_menu():
    print("Enter 'start' or 'exit'")
    command = input().split()
    game_commands = ("user", "easy", "medium", "hard")
    if len(command) == 1 and command[0] == "exit":
        return command
    elif len(command) == 3 and command[0] == "start" and command[1] in game_commands and command[2] in game_commands:
        # print(command)
        return command
    else:
        print("Bad parameters!")
        return game_menu()


def game(board, command):
    game_board.print_game_board(board)
    while game_board.game_state(board) == "Game not finished":

        if command[1] == "user":
            game_board.print_game_board(game_board.player_move_input(board, "X"))
        elif command[1] == "easy":
            print("AI making move level 'easy'")
            ai_1 = ai_player.EasyAi(board, "X")
            game_board.print_game_board(ai_1.easy_ai_move())
        elif command[1] == "medium":
            print("AI making move level 'medium'")
            ai_1 = ai_player.MediumAi(board, "X", "O")
            game_board.print_game_board(ai_1.medium_ai_move())
        else:
            print("AI making move level 'hard'")
            ai_1 = ai_player.HardAi(board, "X", "O")
            game_board.print_game_board(ai_1.hard_ai_move())

        print(game_board.game_state(board))
        if game_board.game_state(board) != "Game not finished":
            break

        if command[2] == "user":
            game_board.print_game_board(game_board.player_move_input(board, "O"))
        elif command[2] == "easy":
            print("AI making move level 'easy'")
            ai_2 = ai_player.EasyAi(board, "O")
            game_board.print_game_board(ai_2.easy_ai_move())
        elif command[2] == "medium":
            print("AI making move level 'medium'")
            ai_2 = ai_player.MediumAi(board, "O", "X")
            game_board.print_game_board(ai_2.medium_ai_move())
        else:
            print("AI making move level 'hard'")
            ai_2 = ai_player.HardAi(board, "O", "X")
            game_board.print_game_board(ai_2.hard_ai_move())

        print(game_board.game_state(board))


if __name__ == "__main__":

    board = game_board.input_initial_board_state()

    menu_command = game_menu()
    while menu_command != ["exit"]:
        game(board, menu_command)
        menu_command = game_menu()
        board = game_board.input_initial_board_state()
