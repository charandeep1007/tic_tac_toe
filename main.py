Board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
winner = None
current_player = "X"
Running = True


def play_game():
    print_board()
    while Running:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()
    if winner == "X" or winner == "O":
        print(winner + "won")
    elif winner == None :
        print("Tie...")


def handle_turn(player):
    print(current_player + "'s turn ")
    position = int(input("enter position fron 0 to 9: "))
    valid = False
    while not valid :
        while position not in range(1, 10):
            position = int(input("enter position from 0 to 9: "))
        position = position - 1
        if Board[position] == "-":
            valid = True
        else:
            print("you cannot go there")
    Board[position] = player
    print_board()


def check_if_game_over():
    check_for_winner()
    check_for_tie()


def check_for_winner():
    global winner
    row_winner = check_for_rows()
    column_winner = check_for_columns()
    diagonal_winner = check_for_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_for_rows():
    global Running
    row_1 = Board[0] == Board[1] == Board[2] != "-"
    row_2 = Board[3] == Board[4] == Board[5] != "-"
    row_3 = Board[6] == Board[7] == Board[8] != "-"
    if row_1 or row_2 or row_3:
        Running = False
    if row_1:
        return Board[0]
    elif row_2:
        return Board[3]
    elif row_3:
        return Board[6]
    else:
        return None


def check_for_columns():
    global Running
    column_1 = Board[0] == Board[3] == Board[6] != "-"
    column_2 = Board[1] == Board[4] == Board[7] != "-"
    column_3 = Board[2] == Board[5] == Board[8] != "-"
    if column_1 or column_2 or column_3 :
        Running = False
    if column_1:
        return Board[0]
    elif column_2:
        return Board[1]
    elif column_3:
        return Board[2]
    else:
        return None


def check_for_diagonals():
    global Running
    diagonal_1 = Board[0] == Board[4] == Board[8] != '-'
    diagonal_2 = Board[2] == Board[4] == Board[6] != '-'
    if diagonal_1 or diagonal_2:
        Running = False
    if diagonal_1:
        return Board[0]
    elif diagonal_2:
        return Board[6]
    else:
        return None


def check_for_tie():
    global Running
    if "-" not in Board:
        Running = False
        return True
    else:
        return False


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


def print_board():
    print(Board[0] + " | " + Board[1] + " | " + Board[2])
    print(Board[3] + " | " + Board[4] + " | " + Board[5])
    print(Board[6] + " | " + Board[7] + " | " + Board[8])


play_game()