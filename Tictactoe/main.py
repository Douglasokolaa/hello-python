# write your code here
empty_cell = " "
valid_cell_values = "XO" + empty_cell
matrix = [[empty_cell for col in range(3)] for row in range(3)]
values = [col for row in matrix for col in row]


def start():
    print_board()
    while not game_finished():
        play()


def play():
    player = "X" if values.count("X") <= values.count("O") else "O"
    position = get_valid_move()
    make_move(position[0], position[1], player)
    print_board()


def game_finished() -> bool:
    finished = True
    if check_won("X") and check_won("O"):
        print("Impossible")
    elif check_won("X"):
        print("X wins")
    elif check_won("O"):
        print("O wins")
    elif empty_cell not in values:
        print("Draw")
    elif not winnable():
        print("Impossible")
    else:
        finished = False
    return finished


def to_matrix_position(position) -> list[int]:
    return [(int(x) - 1) for x in position.split() if x.isnumeric()]


def make_move(x, y, player="X"):
    global values
    matrix[x][y] = player
    values = [col for row in matrix for col in row]


def get_valid_move() -> list[int]:
    valid = False
    move = []

    while not valid:
        cord = input("Enter the coordinates: ")
        move = to_matrix_position(cord)
        if len(move) != 2:
            print("You should enter numbers!")
        elif move[0] < 0 or move[0] > 2 or move[1] < 0 or move[1] > 2:
            print("Coordinates should be from 1 to 3!")
        elif matrix[move[0]][move[1]] != ' ':
            print("This cell is occupied! Choose another one!")
        else:
            valid = True
    return move


def winnable():
    for i in [0, 1, 2]:
        cols = "X" in values[i:(i + 3):(i + 6)] and "O" not in values[i:(i + 3):(i + 6)]
    for i in [0, 1, 2]:
        rows = "X" in values[i:(i + 1):(i + 2)] and "O" not in values[i:(i + 1):(i + 2)]
    diagonals = ("X" in values[0:4:8] and "O" not in values[0:4:8]) or (
            "X" in values[2:4:6] and "O" not in values[2:4:6])

    return any([values.count(empty_cell) <= len(values), cols, rows, diagonals])


def check_won(player):
    return (values[0] == player and values[1] == player and values[2] == player) or (
            values[3] == player and values[4] == player and values[5] == player) or (
                   values[6] == player and values[7] == player and values[8] == player) or (
                   values[0] == player and values[3] == player and values[6] == player) or (
                   values[1] == player and values[4] == player and values[7] == player) or (
                   values[2] == player and values[5] == player and values[8] == player) or (
                   values[0] == player and values[4] == player and values[8] == player) or (
                   values[2] == player and values[4] == player and values[6] == player)


def print_board():
    print("---------")
    print("| {} {} {} |".format(values[0], values[1], values[2]))
    print("| {} {} {} |".format(values[3], values[4], values[5]))
    print("| {} {} {} |".format(values[6], values[7], values[8]))
    print("---------")


start()
