from colorama import Fore, Back, Style



def draw_board(board):

    for x in range(len(board)):

        for y in range(len(board)):
            if board[x][y] == " ":
                if y < len(board) - 1:
                    print(Back.YELLOW + board[x][y] + Style.RESET_ALL, "| ", end='')
                else:
                    print(Back.YELLOW + board[x][y] + Style.RESET_ALL, "| ")
            elif board[x][y] == "X":
                if y < len(board) - 1:
                    print(Fore.RED + 'X' + Style.RESET_ALL, "| ", end='')
                else:
                    print(Fore.RED + 'X' + Style.RESET_ALL, "| ")
            elif board[x][y] == "0":
                if y < len(board) - 1:
                    print(Fore.BLUE + '0'  + Style.RESET_ALL, "| ", end='')
                else:
                    print(Fore.BLUE + '0'  + Style.RESET_ALL, "| ")
                print("---------")



def ask_move(player, board):
    while True:
        try:
            x, y = (
                input(f"{player}, Введите x и y координаты (пример 0 0): ")
                .strip()
                .split()
            )
            x, y = int(x), int(y)
            if (0 <= x < len(board)) and (0 <= y < len(board)) and (board[y][x] == " "):
                return (x, y)
            else:
                print(f"Клетка {x} {y} занята или вне диапазона. Попробуйте еще раз.")
        except ValueError:
            print("Некорректный ввод. Введите два числа, разделенные пробелом.")



def make_move(player, board, x, y):
    board[y][x] = player



def ask_and_make_move(player, board):
    x, y = ask_move(player, board)
    make_move(player, board, x, y)



def check_win(player, board):

    for i in range(len(board)):

        if board[i] == [player, player, player]:
            return True

        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True

        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return True

        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            return True
        return False



def tic_tac_toe(board):

    while True:

        board = [[" " for i in range(board)] for j in range(board)]
        player = "X"
        while True:
            draw_board(board)
            ask_and_make_move(player, board)
            if check_win(player, board):
                print(f"{player} выиграл!")
                break
            if all(cell != " " for row in board for cell in row):
                print("Ничья!")
                break
            player = "0" if player == "X" else "X"
            restart = input("Хотите сыграть еще раз? (y/n)")
            if restart.lower() != "y":
                break