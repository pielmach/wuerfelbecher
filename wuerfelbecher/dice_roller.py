from random import randint
from . import statistics


def roll_dice(number_of_sides: int) -> int:
    dice_roll = randint(1, number_of_sides)
    statistics.add_dice_roll(number_of_sides, dice_roll)
    return dice_roll
