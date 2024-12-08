import random

def hangman():
    # List of words with different difficulty categories
    words = {
        'easy': ['cat', 'dog', 'fish', 'bird', 'apple'],
        'medium': ['python', 'hangman', 'programming', 'developer', 'algorithm'],
        'hard': ['quantum', 'artificial', 'machine', 'neural', 'cryptography']
    }

    # Function to display the hangman drawing based on attempts
    def display_hangman(attempts):
        stages = [
            '''
               -----
               |   |
                   |
                   |
                   |
                   |
              -----
            ''',
            '''
               -----
               |   |
               O   |
                   |
                   |
                   |
              -----
            ''',
            '''
               -----
               |   |
               O   |
               |   |
                   |
                   |
              -----
            ''',
            '''
               -----
               |   |
               O   |
              /|   |
                   |
                   |
              -----
            ''',
            '''
               -----
               |   |
               O   |
              /|\\  |
                   |
                   |
              -----
            ''',
            '''
               -----
               |   |
               O   |
              /|\\  |
              /    |
                   |
              -----
            ''',
            '''
               -----
               |   |
               O   |
              /|\\  |
              / \\  |
                   |
              -----
            '''
        ]
        return stages[attempts]

    # Start of the game
    print("Welcome to Hangman!")

    # Select difficulty
    difficulty = input("Choose difficulty (easy/medium/hard): ").lower()
    if difficulty not in words:
        print("Invalid difficulty. Defaulting to 'medium'.")
        difficulty = 'medium'

    word_to_guess = random.choice(words[difficulty]).lower()
    guessed_word = ['_'] * len(word_to_guess)
    guessed_letters = set()
    max_attempts = 6
    attempts = 0

    print(f"\nThe word has {len(word_to_guess)} letters: {' '.join(guessed_word)}")

    # Game loop
    while attempts < max_attempts and ''.join(guessed_word) != word_to_guess:
        print(display_hangman(attempts))
        guess = input("\nGuess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input! Please enter a single alphabet.")
            continue
        
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print(f"Good job! '{guess}' is in the word.")
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts += 1
            print(f"Attempts remaining: {max_attempts - attempts}")

        print(" ".join(guessed_word))

    # End of game
    if ''.join(guessed_word) == word_to_guess:
        print("\nCongratulations! You've guessed the word correctly!")
    else:
        print(f"\nGame over! The word was '{word_to_guess}'.")

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        hangman()
    else:
        print("Thanks for playing! Goodbye.")

# Run the game
hangman()
