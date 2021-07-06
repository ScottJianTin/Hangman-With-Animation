import time
import random

# Welcome message
print("\nWelcome to Hangman\n")
name = input("What's your name? ")
print("Hello " + name + "! Nice to meet you..\n")
time.sleep(2)
print("The game is about to start! Best of luck!\n Let's play Hangman!\n")
time.sleep(3)

# Main function


def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["steam", "fluctuation", "factor", "socialist", "dilute", "stay",
                      "density", "sweep", "storm", "haircut", "senior", "eye"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = "-" * length
    already_guessed = []
    play_game = ""

# A loop to re-execute the game when first round ends


def play_loop():
    global play_game
    play_game = input("Do you want to play again? y = yes, n = no\n")
    while play_game not in ["Y", "y", "N", "n"]:
        play_game = input("Do you want to play again? y = yes, n = no\n")

    if play_game in ("Y", "y"):
        print("Good luck!")
        main()
        hangman()

    elif play_game in ("N", "n"):
        print("Thanks for playing! We expect you back again")
        exit()  # quit()

# Initialize conditions for Hangman


def hangman():
    global word
    global length
    global display
    global count
    global already_guessed
    global play_game
    limit = 5
    guess = input("\nThis is the Hangman word:" +
                  display + "\nEnter your guess: ")
    guess = guess.strip()

    if len(guess.strip()) == 0 or len(guess.strip()) > 1:
        print("Invalid input, input only one letter\n")
        hangman()

    elif guess in word:
        for correct_char in word:
            if guess == correct_char:
                index = word.find(guess)
                word = word[:index] + "-" + word[index+1:]
                display = display[:index] + guess + display[index+1:]

    elif guess in already_guessed:
        print("You have guessed this letter. Try another letter: ")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |       \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__    \n")
            already_guessed.extend(guess)
            print("Oops, wrong guess. " +
                  str(limit-count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   ____   \n"
                  "  |    |  \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__     \n")
            already_guessed.extend(guess)
            print("Oops, wrong guess. " +
                  str(limit-count) + " guesses remaining\n")

        elif count == 3:
            time.sleep(1)
            print("   ____   \n"
                  "  |    |  \n"
                  "  |    |  \n"
                  "  |    |  \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__     \n")
            already_guessed.extend(guess)
            print("Oops, wrong guess. " +
                  str(limit-count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   ____   \n"
                  "  |    |  \n"
                  "  |    |  \n"
                  "  |    |  \n"
                  "  |    O  \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__     \n")
            already_guessed.extend(guess)
            print("Oops, wrong guess. " +
                  str(limit-count) + " guesses remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   ____   \n"
                  "  |    |  \n"
                  "  |    |  \n"
                  "  |    |  \n"
                  "  |    O  \n"
                  "  |   /|\ \n"
                  "  |   / \ \n"
                  "  |       \n"
                  "__|__     \n")
            already_guessed.extend(guess)
            print("Oops, wrong guess. " +
                  str(limit-count) + " guesses remaining\n")
            print("You lose...")
            play_loop()

    if word == "-"*length:
        print("\nCongratzzzz! You have guess the word correctly!")
        play_loop()

    elif count != limit:
        hangman()


main()
hangman()
