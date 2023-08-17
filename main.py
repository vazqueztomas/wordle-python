from show_guess import show_guess
from game_over import game_over
from user_won_alert import user_won_alert
from get_random_choice import get_random_choice

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
         
         
    

    