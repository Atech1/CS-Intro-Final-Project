# Tilden Winston (tw8rt) Alec Ross(asr3bj) file writing tester
# https://docs.python.org/2/library/random.html


# import IO.py
import file_writing
import random

score = random.randint(0, 100009)
print(score)


file_writing.highscores(int(score))

file_writing.errorlog("here")
# IO.newscore(score)
