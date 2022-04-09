import unittest
from math import isnan

from wuerfelbecher import statistics


class TestStatistics(unittest.TestCase):
    def setUp(self):
        statistics.init_statcounter()

    def test_binomial(self):
        self.assertEqual(statistics.binomial_expectation_value(2, 0.5), 1.0)
        self.assertEqual(statistics.binomial_variance(2, 0.5), 0.5)
        self.assertEqual(statistics.binomial_std_deviations(1, 1.0, 0.5), 0.0)
        self.assertEqual(statistics.binomial_expectation_value(100, 0.05), 5.0)
        self.assertEqual(statistics.binomial_variance(100, 0.05), 4.75)
        self.assertAlmostEqual(statistics.binomial_std_deviations(10, 5.0, 4.75), 2.294157338705618)
        self.assertTrue(isnan(statistics.binomial_std_deviations(10, 5.0, 0.0)))

    def test_statistics(self):
        statistics.add_dice_roll(6, 1)
        statistics.add_dice_roll(6, 2)
        statistics.add_dice_roll(6, 2)
        statistics.add_dice_roll(6, 3)
        statistics.add_dice_roll(6, 4)
        statistics.add_dice_roll(6, 5)
        statistics.add_dice_roll(6, 5)
        statistics.add_dice_roll(6, 5)
        rolls, counts = statistics.get_stats(6)
        self.assertEqual(rolls, 8)
        self.assertEqual(counts[1], 1)
        self.assertEqual(counts[2], 2)
        self.assertEqual(counts[3], 1)
        self.assertEqual(counts[4], 1)
        self.assertEqual(counts[5], 3)
        self.assertEqual(counts[6], 0)

        statistics.init_statcounter()
        rolls, counts = statistics.get_stats(6)
        self.assertEqual(rolls, 0)
        [self.assertEqual(counts[i], 0) for i in range(1, 7)]

        statistics.init_statcounter()
        statistics.add_dice_roll(20, 1)
        statistics.add_dice_roll(20, 5)
        statistics.add_dice_roll(20, 5)
        statistics.add_dice_roll(20, 5)
        statistics.add_dice_roll(20, 20)
        rolls, counts = statistics.get_stats(20)
        self.assertEqual(rolls, 5)
        self.assertEqual(counts[1], 1)
        [self.assertEqual(counts[i], 0) for i in range(2, 5)]
        self.assertEqual(counts[5], 3)
        [self.assertEqual(counts[i], 0) for i in range(6, 20)]
        self.assertEqual(counts[20], 1)


if __name__ == "__main__":
    unittest.main()
