import random

def get_word_hint(secret_word, guess_word):
    secret = secret_word.upper()
    guess = guess_word.upper()
    hint = ""

    for i in range(5):
        if guess[i] == secret[i]:
            hint += "O"
        elif guess[i] in secret:
            hint += "o"
        else:
            hint += "x"

    return hint

words = 'MITTS FLOAT BRICK LIKED DWARF COMMA GNASH ROOMS UNITE BEARS SPOOL ARMOR'.split()
secret_word = random.choice(words)
attempts = 6

print("Welcome to Word Match Game!")
print("You have 6 tries to guess a 5 letter word.")

for attempt in range(1, attempts + 1):
    print(f"\nTry {attempt}: Guess the secret five-letter word:")
    guess = input().strip().upper()

    if len(guess) != 5:
        print("The word must have exactly 5 letters.")
        continue

    hint = get_word_hint(secret_word, guess)
    print(hint)

    if hint == "OOOOO":
        print(f"Congratulations! You guessed the word: {secret_word}")
        break
else:
    print(f"\nNo more attempts. The secret word was: {secret_word}. Better luck next time.")