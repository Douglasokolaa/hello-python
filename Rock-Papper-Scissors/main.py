# Write your code here
import random

options = ['rock', 'paper', 'scissors']
# winner : looser
result = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}

rating = 0


def start():
    name = input("Enter your name: ")
    set_initial_rating(name)
    print("Hello,", name)
    set_options()
    print("Okay, let's start")
    play()


def set_options():
    global options, result
    u_options = input("Enter Options:)
    if u_options:
        options = u_options.split(',')
        result = {}
        for option in options:
            index = options.index(option)
            wins = options[index + 1:] + options[:index]
            result[option] = wins[int((len(wins)) / 2):]


def play():
    while True:
        user_choice = input()
        if user_choice == "!exit":
            break
        elif user_choice == "!rating":
            print_rating()
        elif user_choice not in options:
            print("Invalid input")
            continue
        else:
            print_outcome(user_choice)

    print("Bye")


def print_outcome(user_choice):
    global rating
    computer_choice = random.choice(options)
    if computer_choice == user_choice:
        rating += 50
        print("There is a draw ({})".format(user_choice))
    elif computer_choice in result[user_choice]:
        rating += 100
        print("Well done. The computer chose {} and failed".format(computer_choice))
    else:
        print("Sorry, but the computer chose ", computer_choice)


def set_initial_rating(name: str):
    global rating
    try:
        file = open("rating.txt", 'rt', encoding='utf-8')
        for record in file:
            if name in record:
                rating = int(record.split()[1])
    except FileNotFoundError:
        pass


def print_rating():
    global rating
    print("Your rating:", rating)


start()
