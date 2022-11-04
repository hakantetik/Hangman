from random import choice
import string

win_score = 0
lost_score = 0


def game():
    words = ["python", "java", "swift", "javascript"]
    chosen_word = choice(words)

    word = len(chosen_word) * "-"

    # 8 attempts
    attempts = 8
    print(word)
    guessed_letters = []

    global win_score
    global lost_score

    while attempts > 0:
        letter = input("Input a letter:")

        if len(letter) > 1 or letter == "":
            print("Please, input a single letter.")
            print(word)
            continue
        elif letter.isupper() or letter not in string.ascii_letters:
            print("Please, enter a lowercase letter from the English alphabet.")
            print(word)
            continue
        else:
            guessed_letters.append(letter)

        if guessed_letters.count(letter) > 1:
            print("You've already guessed this letter.")
            print(word)
            continue

        word_list = list(word)
        chosen_word_list = list(chosen_word)

        if letter not in chosen_word:
            print("That letter doesn't appear in the word.")
            attempts -= 1
            print(word)
            continue
        elif letter in chosen_word:
            for index in range(0, len(chosen_word)):
                if chosen_word_list[index] == letter:
                    word_list[index] = letter

            word = "".join(word_list)
            if word == chosen_word:
                print(f"You guessed the word {chosen_word}!")
                print("You survived!")
                win_score += 1
                break

            print(word)
            continue

    if attempts == 0:
        lost_score += 1
        print("You lost!")


game_is_on = True

while game_is_on:
    print("H A N G M A N")
    print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')

    try:
        response = input().lower()
    except response != "play" or "results" or "exit":
        continue

    if response == "play":
        game()
    elif response == "exit":
        game_is_on = False
    elif response == "results":
        print(f"""
        You won: {win_score} times.
        You lost: {lost_score} times.
        """)
        continue
