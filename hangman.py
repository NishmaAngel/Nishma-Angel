import random

# Hangman visual stages
HANGMAN_PICS = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

# Words with their corresponding hints
WORD_DICTIONARY = {
    "python": "A popular programming language named after a snake.",
    "elephant": "The largest existing land animal.",
    "guitar": "A stringed musical instrument played by strumming or plucking.",
    "pizza": "A famous Italian dish with a round base of dough.",
    "pyramid": "An ancient Egyptian structure built as a tomb.",
    "oxygen": "A gas essential for human breathing.",
    "astronomy": "The scientific study of celestial objects and space.",
    "volcano": "A mountain or hill with a crater through which lava erupts."
}

def play_hangman():
    print("Welcome to HANGMAN!")
    
    # Pick a random word and hint
    word = random.choice(list(WORD_DICTIONARY.keys()))
    hint = WORD_DICTIONARY[word]
    
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = len(HANGMAN_PICS) - 1
    
    while incorrect_guesses < max_incorrect_guesses:
        print(HANGMAN_PICS[incorrect_guesses])
        
        # Display the word with guessed letters and underscores for unguessed
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
        
        print(f"Word: {' '.join(display_word)}")
        
        # Check for win condition
        if "_" not in display_word:
            print("\nCongratulations! You guessed the word correctly!")
            print(f"The word was: {word.upper()}")
            return
            
        print("\nOptions:")
        print("1. Guess a letter")
        print("2. Ask for a hint")
        
        choice = input("Enter your choice (1 or 2): ").strip()
        
        if choice == '2':
            print(f"\n---> HINT: {hint} <---")
            continue
        elif choice != '1':
            print("Invalid choice, please enter 1 or 2.")
            continue
            
        guess = input("Guess a letter: ").strip().lower()
        
        # Validation checks
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter from A-Z.")
            continue
            
        if guess in guessed_letters:
            print(f"You've already guessed the letter '{guess}'. Try another one.")
            continue
            
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"\nGood job! '{guess}' is inside the word.")
        else:
            print(f"\nSorry, '{guess}' is not in the word.")
            incorrect_guesses += 1
            
    # If the loop finishes without a win, the player lost
    print(HANGMAN_PICS[-1])
    print("\nGame Over! You've run out of guesses.")
    print(f"The correct word was: {word.upper()}")

if __name__ == "__main__":
    play_hangman()
