import random
from words import words


# from words import words_test

def get_valid_word(words_list):
    valid_word = random.choice(words_list)
    while "-" in valid_word or " " in valid_word:
        valid_word = random.choice(words_list)
    return valid_word


def setup(guessing_word):
    guessing_slots = ""
    counter = 0
    guessing_slots_list = []
    for letter in guessing_word:
        guessing_slots += "_"
        counter += 1
        guessing_slots_list += "_"
    guessing_counter_notification = "The word has " + str(counter) + " letters"
    return guessing_slots, guessing_counter_notification, guessing_slots_list


word = get_valid_word(words)
slots, counter_notification, slots_list = setup(word)
print(slots + "\n" + counter_notification)


def play_hangman(guessing_word, guessing_slots_list):
    counter = 6
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    adjustable_alphabet = "abcdefghijklmnopqrstuvwxyz"
    while counter > 0:
        letter_guess = input("Guess a letter in the word: ").lower()
        print(letter_guess)
        word_reveal = ""
        # Adjusting letter reveal in word
        for index in range(len(guessing_word)):
            if letter_guess in guessing_word[index]:
                guessing_slots_list[index] = letter_guess
        for index in range(len(guessing_slots_list)):
            word_reveal += guessing_slots_list[index]
        # Checking to see if letter has been guessed
        if letter_guess not in alphabet:
            print("Invalid guess. Try again.")
        # Checking to see if character is valid
        elif letter_guess not in adjustable_alphabet:
            print("You guessed this letter already. Try again.")
        # If letter isn't in word
        elif letter_guess not in guessing_word:
            # Remove letter in alphabet
            adjustable_alphabet = adjustable_alphabet.replace(letter_guess, " ")
            counter -= 1
            # Checking losing status
            if counter == 0:
                print("You lost! The word was " + guessing_word)
                break
            print("This letter isn't in the word: " + word_reveal + "\nYou have " + str(counter) + " guesses left.")
        # If letter is in word
        else:
            # Remove letter in alphabet
            adjustable_alphabet = adjustable_alphabet.replace(letter_guess, letter_guess.upper())
            # Checking winning status
            if "_" not in word_reveal:
                print("Congrats you won! The word was " + word_reveal)
                break
            print("This letter is in the word: " + word_reveal + "\nYou have " + str(counter) + " guesses left.")


play_hangman(word, slots_list)
