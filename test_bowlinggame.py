import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def test_gutter_game(self): #changed naming method
        self._roll_many(0, 20)
        self.assertEqual(0, self.game.total_score()) #change assert to self.assertEqual

    def test_all_ones(self): #changed naming method
        self._roll_many(1, 20)
        self.assertEqual(20, self.game.total_score()) #change assert to self.assertEqual

    def test_one_spare(self): #changed naming method
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self._roll_many(0, 17)
        self.assertEqual(16, self.game.total_score()) #change assert to self.assertEqual

    def test_one_strike(self): #changed naming method
        self.game.roll(10)
        self.game.roll(3)
        self.game.roll(4)
        self._roll_many(0, 16)
        self.assertEqual(24, self.game.total_score()) #change assert to self.assertEqual

    def test_perfect_game(self): #changed naming method
        self._roll_many(10, 12)
        self.assertEqual(300, self.game.total_score()) #change assert to self.assertEqual

    def test_one_spare(self): #changed naming method
        self._roll_many(5, 21)
        self.assertEqual(150, self.game.total_score()) #change assert to self.assertEqual

    def _roll_many(self, pins, num): #changed naming method
        for i in range(num):
            self.game.roll(pins) # changed rolls to num 
