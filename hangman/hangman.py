import random
import sys


def game_loop():
    if guess_table == correct_word:
        print("You win!")
        print(*correct_word)
        sys.exit()

    print(*guess_table)
    # print(*correct_word)

    guess = input("Enter a letter: ")

    if guess in guess_table:
        print("You already guessed", guess, "!")

    for index, character in enumerate(correct_word):
        if guess == character:
            guess_table[index] = character

    if guess not in correct_word:
        print("Invalid guess!")

    game_loop()


# Setup
with open("words.txt", "r") as f:
    word_table = [word for line in f for word in line.split()]

word = random.choice(word_table)

correct_word = list(word)
guess_table = []

for i in correct_word:
    guess_table.append("_")

game_loop()
