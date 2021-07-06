import unittest

from wuerfelbecher import dice_roller, statistics


class TestDiceRoll(unittest.TestCase):
    def setUp(self):
        statistics.init_statcounter()

    def test_roll_dice(self):
        results = [1 <= dice_roller.roll_dice(6) <= 6 for _ in range(10000)]
        self.assertTrue(False not in results)
        rolls, _ = statistics.get_stats(6)
        self.assertEqual(rolls, 10000)


if __name__ == "__main__":
    unittest.main()
