from show_guess import show_guess
from game_over import game_over
from user_won_alert import user_won_alert
from get_random_choice import get_random_choice

def main():
    
    word = get_random_choice()
    guesses = ["_" * 5] * 6 

    for idx in range(6):
      guesses[idx] = input(f"\nGuess {idx + 1}: ").upper()
  
      show_guess(guesses[idx], word)
      if guesses[idx] == word:
         user_won_alert(guesses[idx])
         break
    else:
      game_over(word)


if __name__ == "__main__":
   main()
         
         
    

    