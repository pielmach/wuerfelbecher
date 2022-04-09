import unittest

from wuerfelbecher import commands, statistics


class TestCommands(unittest.TestCase):
    def setUp(self):
        statistics.init_statcounter()

    def test_roll(self):
        self.assertTrue(commands.roll("d2") in ["[ **1** ]", "[ **2** ]"])
        self.assertTrue(commands.roll("D2") in ["[ **1** ]", "[ **2** ]"])
        self.assertTrue(commands.roll("w2") in ["[ **1** ]", "[ **2** ]"])
        self.assertTrue(commands.roll("W2") in ["[ **1** ]", "[ **2** ]"])
        self.assertTrue(commands.roll(" d2") in ["[ **1** ]", "[ **2** ]"])
        self.assertTrue(commands.roll("d2 ") in ["[ **1** ]", "[ **2** ]"])
        self.assertTrue(commands.roll("d2-1") in ["[ **1** ]-1=**0**", "[ **2** ]-1=**1**"])
        self.assertTrue(commands.roll("d2+1") in ["[ **1** ]+1=**2**", "[ **2** ]+1=**3**"])
        self.assertTrue(commands.roll("2d2") in ["[ **1  1** ]", "[ **1  2** ]", "[ **2  1** ]", "[ **2  2** ]"])
        self.assertTrue(
            commands.roll("2d2-1")
            in ["[ **1  1** ]-1=**1**", "[ **1  2** ]-1=**2**", "[ **2  1** ]-1=**2**", "[ **2  2** ]-1=**3**"]
        )
        self.assertTrue(
            commands.roll("2d2+") in ["[ **1  1** ]=**2**", "[ **1  2** ]=**3**", "[ **2  1** ]=**3**", "[ **2  2** ]=**4**"]
        )
        self.assertTrue(
            commands.roll("2d2+0") in ["[ **1  1** ]=**2**", "[ **1  2** ]=**3**", "[ **2  1** ]=**3**", "[ **2  2** ]=**4**"]
        )
        self.assertTrue(
            commands.roll("d2 d2")
            in ["[ **1** ]  [ **1** ]", "[ **1** ]  [ **2** ]", "[ **2** ]  [ **1** ]", "[ **2** ]  [ **2** ]"]
        )
        self.assertTrue(
            commands.roll(" ".join(["d2", "d2"]))
            in ["[ **1** ]  [ **1** ]", "[ **1** ]  [ **2** ]", "[ **2** ]  [ **1** ]", "[ **2** ]  [ **2** ]"]
        )
        self.assertEqual(commands.roll("foo"), "You shall not pass! Ask for *!help* if you fear my power!")
        self.assertEqual(commands.roll("d2!"), "You shall not pass! Ask for *!help* if you fear my power!")
        self.assertEqual(commands.roll("!w2"), "You shall not pass! Ask for *!help* if you fear my power!")
        self.assertEqual(commands.roll("d0"), "You shall not pass! Ask for *!help* if you fear my power!")

    def test_stats(self):
        self.assertEqual(
            commands.stats("d2"),
            "```You rolled the d2 0 times. Those are the results including how many standard deviations (σ) the result deviates from the expectation value:\n  1:   0  (nanσ)\n  2:   0  (nanσ)\n```",
        )
        self.assertEqual(
            commands.stats("W2"),
            "```You rolled the d2 0 times. Those are the results including how many standard deviations (σ) the result deviates from the expectation value:\n  1:   0  (nanσ)\n  2:   0  (nanσ)\n```",
        )
        self.assertEqual(commands.stats("foo"), "You shall not pass! Ask for *!help* if you fear my power!")


if __name__ == "__main__":
    unittest.main()
