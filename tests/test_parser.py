import unittest
from wuerfelbecher import parser
from wuerfelbecher import statistics

class TestParser(unittest.TestCase):
    def setUp(self):
        statistics.init_statcounter()

    def test_parse_roll(self):
        self.assertEqual(parser.parse_roll('d6'), [parser.SetToRoll(1, 6, None)])
        self.assertEqual(parser.parse_roll('w6'), [parser.SetToRoll(1, 6, None)])
        self.assertEqual(parser.parse_roll('1d6'), [parser.SetToRoll(1, 6, None)])
        self.assertEqual(parser.parse_roll('1w6'), [parser.SetToRoll(1, 6, None)])
        self.assertEqual(parser.parse_roll('2d6'), [parser.SetToRoll(2, 6, None)])
        self.assertEqual(parser.parse_roll('2w6'), [parser.SetToRoll(2, 6, None)])
        self.assertEqual(parser.parse_roll('3d20'), [parser.SetToRoll(3, 20, None)])
        self.assertEqual(parser.parse_roll('3w20'), [parser.SetToRoll(3, 20, None)])

        self.assertEqual(parser.parse_roll('d6+2'), [parser.SetToRoll(1, 6, 2)])
        self.assertEqual(parser.parse_roll('w6-2'), [parser.SetToRoll(1, 6, -2)])
        self.assertEqual(parser.parse_roll('2d6-4'), [parser.SetToRoll(2, 6, -4)])
        self.assertEqual(parser.parse_roll('2w6+4'), [parser.SetToRoll(2, 6, 4)])
        self.assertEqual(parser.parse_roll('3d20+10'), [parser.SetToRoll(3, 20, 10)])
        self.assertEqual(parser.parse_roll('3w20-10'), [parser.SetToRoll(3, 20, -10)])

        self.assertEqual(parser.parse_roll('2d6+'), [parser.SetToRoll(2, 6, 0)])
        self.assertEqual(parser.parse_roll('2w6-'), [parser.SetToRoll(2, 6, 0)])
        self.assertEqual(parser.parse_roll('2d6+0'), [parser.SetToRoll(2, 6, 0)])
        self.assertEqual(parser.parse_roll('2w6-0'), [parser.SetToRoll(2, 6, 0)])

        self.assertEqual(parser.parse_roll('12+w6'), [parser.SetToRoll(1, 6, 12)])
        self.assertEqual(parser.parse_roll('12+2w6'), [parser.SetToRoll(2, 6, 12)])
        self.assertEqual(parser.parse_roll('-1+2w6'), [parser.SetToRoll(2, 6, -1)])

        self.assertEqual(parser.parse_roll('w20 2w6+2'), [parser.SetToRoll(1, 20, None), parser.SetToRoll(2, 6, 2)])
        self.assertEqual(parser.parse_roll('w20 2w6+2 '), [parser.SetToRoll(1, 20, None), parser.SetToRoll(2, 6, 2)])
        self.assertEqual(parser.parse_roll(' w20 2w6+2'), [parser.SetToRoll(1, 20, None), parser.SetToRoll(2, 6, 2)])
        self.assertEqual(parser.parse_roll(' w20  2w6+2 '), [parser.SetToRoll(1, 20, None), parser.SetToRoll(2, 6, 2)])
        self.assertEqual(parser.parse_roll('  w20  2w6+2  '), [parser.SetToRoll(1, 20, None), parser.SetToRoll(2, 6, 2)])

        with self.assertRaises(ValueError):
            parser.parse_roll('foo')
        with self.assertRaises(ValueError):
            parser.parse_roll('d6 +4')
        with self.assertRaises(ValueError):
            parser.parse_roll('d6+4!')
        with self.assertRaises(ValueError):
            parser.parse_roll('4+d6+4')
        with self.assertRaises(ValueError):
            parser.parse_roll('w20 2w6+2!')
        with self.assertRaises(ValueError):
            parser.parse_roll('w20,2w6+2')
        with self.assertRaises(ValueError):
            parser.parse_roll('w20;2w6+2')

    def test_parse_stats(self):
        self.assertEqual(parser.parse_stats('d6'), 6)
        self.assertEqual(parser.parse_stats('w20'), 20)
        self.assertEqual(parser.parse_stats(' d6 '), 6)
        self.assertEqual(parser.parse_stats(' w6'), 6)
        self.assertEqual(parser.parse_stats(' w6 '), 6)
        with self.assertRaises(ValueError):
            parser.parse_stats('foo')
        with self.assertRaises(ValueError):
            parser.parse_stats('w6+2')
        with self.assertRaises(ValueError):
            parser.parse_stats('d20w6')
        with self.assertRaises(ValueError):
            parser.parse_stats('d20 w6')

if __name__ == '__main__':
    unittest.main()