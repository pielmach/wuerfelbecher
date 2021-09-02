from . import dice_roller, parser, statistics


def roll(message: str) -> str:
    try:
        sets_to_roll = parser.parse_roll(message.lower())
        result = ""
        for s in sets_to_roll:
            result += "  "
            rolls = []
            for _ in range(s.count):
                rolls.append(dice_roller.roll_dice(s.dice_type))
            result += "[ **" + "  ".join([str(i) for i in rolls]) + "** ]"
            if s.modifier is not None:
                sum_of_rolls = sum(rolls)
                if s.modifier > 0:
                    result += "+" + str(s.modifier)
                elif s.modifier < 0:
                    result += str(s.modifier)
                result += "=**" + str(sum_of_rolls + s.modifier) + "**"
        return result.lstrip().rstrip()
    except ValueError:
        return "You shall not pass! Ask for *!help* if you fear my power!"


def stats(message: str) -> str:
    try:
        number_of_sides = parser.parse_stats(message.lower())
        rolls, counts = statistics.get_stats(number_of_sides)
        return "You rolled {0} times and those were the rolls:\n>>> {1}".format(
            rolls,
            "".join(["{0}: {1}\n".format(i, counts[i]) for i in range(1, number_of_sides + 1)]),
        )
    except ValueError:
        return "You shall not pass! Ask for *!help* if you fear my power!"
