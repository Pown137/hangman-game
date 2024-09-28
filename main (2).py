import random

def hangman_game():
    words = ["python", "hangman", "challenge", "programming", "developer"]
    word_to_guess = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to 'Hangman Challenge'!")
    
    while attempts > 0:
        current_state = ''.join([letter if letter in guessed_letters else '_' for letter in word_to_guess])
        print(f"Word: {current_state}")
        print(f"Attempts left: {attempts}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word_to_guess:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            guessed_letters.append(guess)
            attempts -= 1
            print("Wrong guess!")

        if all(letter in guessed_letters for letter in word_to_guess):
            print(f"Congratulations! You've guessed the word: {word_to_guess}")
            break

    if attempts == 0:
        print(f"Game over! The word was: {word_to_guess}")

hangman_game()
