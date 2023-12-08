import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):
    """
    A unittest.TestCase subclass for testing the BowlingGame class.

    This test class covers various scenarios in a typical game of bowling,
    including gutter games, games with all rolls knocking down only one pin,
    games with spares, strikes, and a perfect game.

    Methods:
    --------
    setUp():
        Initialises the BowlingGame instance before each test method.

    test_gutter_game():
        Tests a game where every roll knocks down zero pins.

    test_all_ones():
        Tests a game where every roll knocks down one pin.

    test_one_spare():
        Tests a game with one spare followed by a regular roll.

    test_one_strike():
        Tests a game with one strike followed by two regular rolls.

    test_perfect_game():
        Tests a perfect game with strikes only.

    test_one_spare():
        Tests a game with a continuous sequence of spares.

    _roll_many(pins : int, num : int):
        A helper method for rolling the ball a specified number of times.
    """

    def setUp(self):
        """
        Initializes a new instance of BowlingGame before each test.
        """
        self.game = BowlingGame.BowlingGame()

    def test_gutter_game(self): 
        """
        Tests a gutter game where no pins are knocked down in any roll.
        """
        self._roll_many(0, 20)
        self.assertEqual(0, self.game.total_score())

    def test_all_ones(self): 
        """
        Tests a game where each roll knocks down one pin.
        """
        self._roll_many(1, 20)
        self.assertEqual(20, self.game.total_score())

    def test_one_spare(self): 
        """
        Tests a game with a spare in the first frame, followed by a regular roll, then gutter balls.
        """
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self._roll_many(0, 17)
        self.assertEqual(16, self.game.total_score())

    def test_one_strike(self): 
        """
        Tests a game with a strike in the first roll, followed by two regular rolls, then gutter balls.
        """
        self.game.roll(10)
        self.game.roll(3)
        self.game.roll(4)
        self._roll_many(0, 16)
        self.assertEqual(24, self.game.total_score())

    def test_perfect_game(self): 
        """
        Tests a perfect game with a continuous sequence of strikes.
        """
        self._roll_many(10, 12)
        self.assertEqual(300, self.game.total_score())

    def test_one_spare(self): 
        """
        Tests a game with a continuous sequence of spares.
        """
        self._roll_many(5, 21)
        self.assertEqual(150, self.game.total_score())

    def _roll_many(self, pins, num): 
        """
        A helper method to roll the ball a specified number of times with a specified number of pins.

        Parameters:
        -----------
        pins : int
            The number of pins knocked down in each roll.

        num : int
            The number of times to roll.
        """
        for i in range(num):
            self.game.roll(pins)
