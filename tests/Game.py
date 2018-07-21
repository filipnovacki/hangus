import unittest
from src.Logic.Game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game("solution")

    def test_nonLetter_should_raiseException(self):
        with self.assertRaises(Exception):
            self.game = Game("non Letter $ign")

    def test_spacesinput_should_faltyAndNonyGuessedList(self):
        self.game = Game("very many spaces are in here")
        self.assertEqual(5, (self.game.guessed).count(None))

    def test_lowScore_should_loseGame(self):
        self.game = Game("anything")
        self.game.score = 0
        self.assertFalse(self.game.victory)

    def test_falseInput_shuold_reduceScore(self):
        self.game = Game("anything")
        score = self.game.score
        self.game.guess = "z"
        self.assertEqual(self.game.score, score-1)

    def test_tooManyInput_should_doNothing(self):
        score = self.game.score
        self.game.guess="ah"
        self.assertEqual(score, self.game.score)

    def test_GuessingLetter_should_removeLetterFromAvailableLetters(self):
        self.game = Game("really anything")
        self.game.guess = "u"
        self.assertNotIn("u", self.game.availableLetters)

    def test_capitalisedInput_shuold_Decapitalise(self):
        self.game= Game("I aM lOoDaChA")
        self.assertEqual(self.game.solution, "i am loodacha")