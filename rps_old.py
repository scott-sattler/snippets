# basic 1 line rock paper scissors game
from random import choice; [[input('Choose Rock Paper or Scissors: '), print(choice(["win", "lose", "tie"]))] for i in range(int(input('How many games to play? ')))] # noqa
