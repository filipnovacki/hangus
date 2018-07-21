def solution(game_guess):
    print(" ".join(game_guess))


def letters(al):
    print("Available letters for guessing: {}".format(", ".join(al)))


def score(score):
    print("Moves left: {}".format(score))


def show(game):
    solution(game.guess)
    letters(game.availableLetters)
    score(game.score)
