import unittest
from .main import SnakesLadders

game = SnakesLadders()


class TestGame(unittest.TestCase):

    def test_case_example(self):
        self.assertEqual(game.play(1, 1), "Player 1 is on square 38")

        self.assertEqual(game.play(1, 5), "Player 1 is on square 44")

        self.assertEqual(game.play(6, 2), "Player 2 is on square 31")

        self.assertEqual(game.play(1, 1), "Player 1 is on square 25")


if __name__ == '__main__':
    unittest.main()
