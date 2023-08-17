import string
def show_guess(guesses, word: str):
    styled_guesses = []
    correct_letters = []
    misplaced_letters = []
    wrong_letters = []
    for guess in guesses:
        for letter, correct in zip(guess, word):
            if letter == correct:
                correct_letters.append(letter)
            elif letter in word:
                misplaced_letters.append(letter)
            elif letter in string.ascii_letters:
                wrong_letters.append(letter)
        styled_guesses.append(f"{letter}")

    print("".join(styled_guesses))
    print("Correct letters:", ", ".join(sorted(correct_letters)))
    print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
    print("Wrong letters:", ", ".join(sorted(wrong_letters)))
