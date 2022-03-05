# Write your code here
from random import shuffle, choice, randint

user_turn_msg = "It's your turn to make a move. Enter your command."
computer_turn_msg = 'Computer is about to make a move. Press Enter to continue...'


def main():
    result = []
    result, stock, computer, user, second_player = init(result)
    play(result, stock, computer, user, second_player)


def init(result):
    while True:
        full_set = get_full_set()
        computer, stock, user = full_set[:7], full_set[7:21], full_set[21:]
        snake = get_snake(computer + stock + user)
        message, next_player = get_next_player(snake, computer, user)

        # Reduce
        if next_player:
            reduce_pieces(snake, next_player, computer, user)
            result.append(snake)
            break

    print_status(stock, computer, user, result, message)

    return result, stock, computer, user, next_player


def play(result, stock, computer, user, second_player):
    if second_player == computer:
        result, stock, computer = make_computer_move(result, stock, computer)
        print_status(stock, computer, user, result, user_turn_msg)

    while True:
        end, message = should_end_game(result, computer, user)
        if end:
            print_status(stock, computer, user, result, message)
            break

        move = get_user_move(result, user)
        result, stock, user = make_move(result, stock, user, move)

        end, message = should_end_game(result, computer, user)
        if not end:
            print_status(stock, computer, user, result, computer_turn_msg)
            result, stock, computer = make_computer_move(result, stock, computer)

        end, message = should_end_game(result, computer, user)
        if not end:
            print_status(stock, computer, user, result, user_turn_msg)

    return result, stock, computer, user


def validate_move(result, player, move):
    if move == 0:
        return True
    if len(player) == 1:
        snake = player[0]
    else:
        snake = player[abs(move) - 1]

    last_item = len(result) - 1
    if (snake[0] in result[0]) or (snake[1] in result[0]) or (snake[0] in result[last_item]) or (
            snake[1] in result[last_item]):
        return True
    return False


def make_move(result: list, stock: list, player: list, move: int):
    if move == 0 and len(stock) == 0:
        return result, stock, player

    if len(player) == 1 and move == 1:
        snake = player[0]
    else:
        snake = player[abs(move) - 1]

    if move == 0:
        extra = choice(stock)
        stock.remove(extra)
        player.append(extra)
    elif move < 0:
        player.remove(snake)
        result.insert(0, snake)
    elif move > 0:
        result.append(snake)
        player.remove(snake)
    return result, stock, player


def make_computer_move(result, stock, computer):
    input()
    book = [{'piece': piece, 'sum': sum([computer.count(value) + result.count(value) for value in piece])} for piece in computer]
    book = sorted(book, key=lambda item: item['sum'], reverse=True)

    for i in book:
        index = computer.index(i['piece']) + 1
        if validate_move(result=result, move=index, player=computer):
            return make_move(result, stock, computer, index)
    else:
        index = 0
    return make_move(result, stock, computer, index)


def reduce_pieces(snake, next_player, computer, user) -> tuple[list[int], list[int]]:
    if next_player == computer:
        user.remove(snake)
    else:
        computer.remove(snake)
    return computer, user


def should_end_game(result, computer, user):
    if len(computer) == 0:
        return True, "The game is over. The computer won!"
    if len(user) == 0:
        return True, "The game is over. You won!"
    last_item = len(result) - 1
    if result[0][0] in result[last_item] or result[0][1] in result[last_item]:
        if [item for piece in result for item in piece].count(result[0][0]) == 8:
            return True, "The game is over. It's a draw!"
    return False, ''


def get_user_move(result, user_pieces):
    length = len(user_pieces)
    while True:
        try:
            move = int(input())
            if -length <= move <= length:
                move = move if (move < length) or (length == 1 and move == 1) else move
                if validate_move(result=result, move=move, player=user_pieces):
                    return move
                print("Illegal move. Please try again.")
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")
            continue


def get_snake(full_set):
    return max(full_set)


def get_next_player(snake: list[int], computer: list[int], user: list[int]) -> tuple[str, list]:
    if snake in computer:
        message = user_turn_msg
        return message, user
    elif snake in user:
        message = computer_turn_msg
        return message, computer
    return '', []


def get_full_set() -> list:
    full_set = [[x, y] for x in range(7) for y in range(x + 1)]
    shuffle(full_set)
    return full_set


def get_pieces(full_set: list, num):
    return full_set[:num], full_set[num:]


def print_status(stock: list, computer: list, user: list, result: list, message: str):
    print_header()
    print("Stock size:", len(stock))
    print("Computer pieces:", len(computer))
    print_result(result)
    print_user_pieces(user)
    print_next_player(message)


def print_header():
    print(70 * "=")


def print_result(result):
    print()

    if len(result) <= 6:
        print("".join([str(item) for item in result]))
    else:
        print("".join([str(item) for item in result[:3]]), end="...")
        print("".join([str(item) for item in result[-3:]]))


def print_user_pieces(pieces):
    print()
    print("Your pieces:\n", *["{}:{} \n".format(i + 1, piece) for i, piece in enumerate(pieces)])


def print_next_player(message):
    print("Status: ", message)


main()
