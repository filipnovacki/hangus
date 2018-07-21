from src.Logic import Game
from src.Display import GameShow

try:
    g = Game.Game(input("Let's play a game! Enter a word: "))
except Exception as e:
    print(repr(e))
    exit()

while g.gameLasts:
    GameShow.show(g)
    g.guess = input("Please guess a letter")

else:
    if g.victory:
        GameShow.show(g)
        print("Congratulations on victory")
    else:
        GameShow.show(g)
        print("You lose :(")
        print(g.solution + " is solution of the game.")