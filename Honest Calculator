# write your code here
from math import remainder

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
operators = '+-*/'
memory = 0

msg_ = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]


def check(v1: float, v2: float, v3: str):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6

    if v1 == 1 or v2 == 1:
        msg += msg_7

    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg += msg_8

    if msg != "":
        msg = msg_9 + msg
    print(msg)


def is_one_digit(v: float) -> bool:
    return -10 < v < 10 and v.is_integer()


while True:
    print(msg_0)
    x, operator, y = input().split()

    if x == "M":
        x = memory
    if y == "M":
        y = memory
    try:
        x, y = float(x), float(y),

        if operators.find(operator) == -1:
            print(msg_2)
            continue

        check(x, y, operator)

        if operator == "+":
            result = sum([x, y])
        elif operator == "-":
            result = x - y
        elif operator == "*":
            result = x * y
        else:
            result = x / y
    except ValueError:
        print(msg_1)
        continue
    except ZeroDivisionError:
        print(msg_3)
        continue
    else:
        if result == -5.0:
            result = abs(result)
        print(result)
        while True:
            print(msg_4)
            answer = input()
            if answer == "y":
                if is_one_digit(result):
                    msg_index = 10
                    while True:
                        print(msg_[msg_index])
                        answer = input()
                        if answer == "y":
                            if msg_index < 12:
                                msg_index = msg_index + 1
                                continue
                            else:
                                break
                        elif answer != "n":
                            continue
                        break
                memory = result
            elif answer != "n":
                continue
            break

        calc = False
        while True:
            print(msg_5)
            answer = input()
            if answer == "n":
                break
            elif answer == "y":
                calc = True
                break
        if calc:
            continue
    break
