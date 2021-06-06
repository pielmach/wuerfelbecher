from collections import Counter
from collections import defaultdict

__statcounter__ = None


def add_dice_roll(number_of_sides: int, dice_roll: int):
    global __statcounter__
    __statcounter__[number_of_sides][dice_roll] += 1


def get_stats(number_of_sides: int) -> (int, Counter):
    global __statcounter__
    return sum(__statcounter__[number_of_sides].values()), __statcounter__[number_of_sides]


def init_statcounter():
    global __statcounter__
    __statcounter__ = defaultdict(Counter)


init_statcounter()
