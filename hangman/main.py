# Write your code here
import random

random.seed()
tries = 8

print("H A N G M A N")

while True:
    action = input('Type "play" to play the game, "exit" to quit:')
    if action == 'exit':
        exit()
    elif action == 'play':
        break


print()
words = ['python', 'java', 'kotlin', 'javascript']
selected = random.choice(words)
guess = '-' * len(selected)
identified = list(guess)
feedback = ""
usedLetters = []

print(guess)
while tries > 0:
    feedback = ""
    reduce = False
    letter = input("Input a letter:")
    if len(letter) > 1:
        feedback = "You should input a single letter"
    elif not letter.isalpha() or letter.isupper():
        feedback = "Please enter a lowercase English letter"
    elif selected.find(letter) != -1:
        if letter in identified:
            feedback = "You've already guessed this letter"
        for index, x in enumerate(identified):
            if selected[index] == letter:
                identified[index] = letter
        guess = ''.join(identified)
    elif letter in usedLetters:
        feedback = "You've already guessed this letter"
    else:
        feedback = "That letter doesn't appear in the word"
        reduce = True

    usedLetters.append(letter)
    print(feedback)
    if reduce:
        tries -= 1

    if tries > 0:
        print()
        print(guess)

    if guess == selected:
        print("You guessed the word!")
        print("You survived!")
        break
else:
    print("You lost!")
