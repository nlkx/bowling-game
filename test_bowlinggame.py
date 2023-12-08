import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def test_gutter_game(self):
        self._roll_many(0, 20)
        self.assertEqual(0, self.game.total_score())

    def test_all_ones(self):
        self._roll_many(1, 20)
        self.assertEqual(20, self.game.total_score())