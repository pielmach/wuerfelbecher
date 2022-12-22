from collections import Counter, defaultdict
from math import fabs, nan, sqrt
from typing import DefaultDict, Tuple  # noqa: F401

__statcounter__ = defaultdict(Counter)  # type: DefaultDict[int, Counter]


def binomial_expectation_value(n: int, p: float) -> float:
    return n * p


def binomial_variance(n: int, p: float) -> float:
    return n * p * (1 - p)


def binomial_std_deviations(observed: int, expectation: float, variance: float) -> float:
    if variance <= 0.0:
        return nan
    return fabs(observed - expectation) / sqrt(variance)


def add_dice_roll(number_of_sides: int, dice_roll: int) -> None:
    global __statcounter__
    __statcounter__[number_of_sides][dice_roll] += 1  # type: ignore


def get_stats(number_of_sides: int) -> Tuple[int, Counter]:
    global __statcounter__
    return sum(__statcounter__[number_of_sides].values()), __statcounter__[number_of_sides]  # type: ignore


def init_statcounter() -> None:
    global __statcounter__
    __statcounter__ = defaultdict(Counter)
