import random
import pathlib

def get_random_choice():
    WORDLIST = pathlib.Path("wordlist.txt").read_text(encoding='utf-8').upper().strip().split("\n")
    return random.choice(WORDLIST)

