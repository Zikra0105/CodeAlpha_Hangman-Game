import random

# List of words to choose from
words = ["python", "hangman", "challenge", "computer", "science", "programming", "artificial"]

# Select a random word
word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("🎉 Welcome to Hangman!")
print("_ " * len(word))

while incorrect_guesses < max_attempts:
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Good guess!")
    else:
        incorrect_guesses += 1
        print(f"❌ Wrong guess! Attempts left: {max_attempts - incorrect_guesses}")

    # Display the word with guessed letters
    display_word = ""
    for letter in word:
        display_word += letter + " " if letter in guessed_letters else "_ "
    print(display_word.strip())

    # Check for win
    if all(letter in guessed_letters for letter in word):
        print("🎊 Congratulations! You guessed the word:", word)
        break
else:
    print("💀 Game Over! The word was:", word)
