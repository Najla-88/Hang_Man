# first install this package ...
# pip install termcolor

from random import randint
from termcolor import colored


def hangMan():
    # list of words
    word_list = ["attack", "bnha", "stone", "jjk", "onepiece"]

    # random index for list
    rand_index = randint(0, len(word_list) - 1)

    # random word to guess
    random_word = word_list[rand_index]

    # List of gussed letters
    guessed_letters = ["_" for _ in range(0, len(random_word))]

    # counter calculates wrong tries
    counter = 5

    # loop until guess the word or allowed tries end
    while counter > 0:
        print(f"allowed tries: {counter}")

        # temp variable to remove right characters from it
        temp_word = random_word

        print(colored(" guess anime name ".center(50, "*").title(), color="blue"))
        print("Fill these spaces with the right characters:")

        # print right and remaining characters of the word in one line
        for i in guessed_letters:
            print(i, end=" ")

        # resieve one character from user by take just the first index
        input_char = input("\nEnter one character: ").lower().strip()[0]

        # chick if the input char in the word
        if input_char in temp_word and input_char not in guessed_letters:
            # search for this char in whole world
            for i in temp_word:
                if i == input_char:
                    # when find the character in the word and store its index
                    letter_index = temp_word.index(i)

                    # remove the character from the temp var so we can get the index
                    # of the next same character if
                    temp_word = temp_word.replace(temp_word[letter_index], " ", 1)

                    # put the input char in the correct position of the list
                    guessed_letters[letter_index] = input_char

        else:
            # if the character is wrong or user entered it before decrease allowed tries by one
            counter -= 1

        # check if user guess the word
        if "_" not in guessed_letters:
            print(colored("\nWOW, you win >_<", color="green"))
            print(
                f"\nThe Anime name was {colored( random_word.upper(), color='yellow' )}"
            )
            # break the loop when guess the word
            break

    else:
        print(colored("\nSorry, you lose.", color="red"))


# restart the game untill user exit
while input("\nEnter 'S' to start the game: ").lower() == "s":
    hangMan()
    print("Try again ?")
