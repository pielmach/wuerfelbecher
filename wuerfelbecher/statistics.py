from collections import Counter, defaultdict
from typing import DefaultDict, Tuple

__statcounter__ = defaultdict(Counter)  # type: DefaultDict[int, Counter]


def add_dice_roll(number_of_sides: int, dice_roll: int) -> None:
    global __statcounter__
    __statcounter__[number_of_sides][dice_roll] += 1  # type: ignore


def get_stats(number_of_sides: int) -> Tuple[int, Counter]:
    global __statcounter__
    return sum(__statcounter__[number_of_sides].values()), __statcounter__[number_of_sides]  # type: ignore


def init_statcounter() -> None:
    global __statcounter__
    __statcounter__ = defaultdict(Counter)
