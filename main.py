import pathlib
import random

def get_random_choice():
    WORDLIST = pathlib.Path("wordlist.txt").read_text(encoding='utf-8').upper().strip().split("\n")
    return random.choice(WORDLIST)

def show_guess(guess, word: str):
    """Show the user's guess on the terminal and classify all letters.

    ## Example:

    >>> show_guess("CRANE", "SNAKE")
    Correct letters: A, E
    Misplaced letters: N
    Wrong letters: C, R
    """
    correct_letters = {
        letter for letter, correct in zip(guess, word) if letter == correct
    }
    misplaced_letters = set(guess) & set(word) - correct_letters
    wrong_letters = set(guess) - set(word)

    print("Correct letters:", ", ".join(sorted(correct_letters)))
    print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
    print("Wrong letters:", ", ".join(sorted(wrong_letters)))

def game_over(word: str):
   """Show the game over message
  
    ## Example:
    >>> game_over("QUAKE")
    The word was QUAKE
   """
   print(f'The word was {word}')

def user_won_alert(word: str):
   """
    Show the won message to the user
    >>> user_won_alert("QUAKE")
    You won this game! The word is: QUAKE
   """
   print(f'You won this game! The word is: {word}')
   

def main():
    
    word = get_random_choice()

    for guess_num in range(1, 7):
      guess = input(f"\nGuess {guess_num}: ").upper()
  
      show_guess(guess, word)
      if guess == word:
         user_won_alert(guess)
         break
    else:
      game_over(word)


if __name__ == "__main__":
   main()
         
         
    

    