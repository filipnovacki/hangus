from string import ascii_lowercase as al


class Game:
    def __init__(self, solution):
        self.solution = self.transform_solution(solution)
        if self.solution is False:
            raise Exception("Input must contain only letters and spaces")
        self.guessed = [None if ch == " " else False for ch in solution]
        self.available = list(al)
        self.score = 10

    @property
    def victory(self):
        if self.score > 0:
            return True
        else:
            return False

    @property
    def gameLasts(self):
        if self.score > 0 and not self.guessed_all():
            return True
        else:
            return False

    @property
    def guess(self):
        """Property that handles guessed letters in solution, returns string of solution displayable to player"""
        guessedLetters = ""
        for i, ch in zip(self.guessed, self.solution):
            if i:
                guessedLetters += ch
            elif ch == " ":
                guessedLetters += " "
            else:
                guessedLetters += "_"
        return guessedLetters

    @guess.setter
    def guess(self, letter):
        """Checks if the input letter is in solution"""
        # ie letter has already been chosen
        guessed = False
        if len(letter) > 1:
            return
        if letter not in self.availableLetters:
            print("Invalid letter input")
            return
        for i, ch in enumerate(self.solution):
            if ch == letter:
                self.guessed[i] = True
                guessed = True
        self.availableLetters = letter
        if not guessed:
            self.score -= 1

    @property
    def availableLetters(self):
        return self.available

    @availableLetters.setter
    def availableLetters(self, ch):
        """When guessing, removes letter from potentially possible letters"""
        self.available.remove(ch)

    @staticmethod
    def transform_solution(sol):
        # Transforms all letters to lowercase
        sol = sol.lower()
        for x in sol:
            if x not in al and x != " ":
                return False
        return sol

    def guessed_all(self):
        for i in self.guessed:
            if i == False:
                return False
        return True
