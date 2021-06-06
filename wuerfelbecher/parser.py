import re
from collections import namedtuple

SetToRoll = namedtuple('SetToRoll', ['count', 'dice_type', 'modifier'])


def _translate_dice_pattern_match(match: re.Match) -> SetToRoll:
    count = 1 if match.group(1) is None else int(match.group(1))
    dice_type = int(match.group(2))
    modifier = None
    if match.group(3) in ('+', '-'):
        modifier = 0
    elif match.group(3) != '':
        modifier = int(match.group(3))
    return SetToRoll(count, dice_type, modifier)


def _translate_dice_pattern_inverse_match(match: re.Match) -> SetToRoll:
    count = 1 if match.group(2) is None else int(match.group(2))
    dice_type = int(match.group(3))
    modifier = int(match.group(1))
    return SetToRoll(count, dice_type, modifier)


def parse_roll(message: str) -> [SetToRoll]:
    '''Parses the message of the roll command. The applied strategy is:

    1. Try the regular dice pattern e.g. 2d6+10
    2. Try the inverse dice pattern e.g. 10+2d6
    3. Split message on spaces and do a recursive attempt for each split, if one split fails, entire message fails
    '''
    stripped_message = message.lstrip().rstrip()

    dice_pattern_match = re.match(r'^([1-9][0-9]*)?[dw]([1-9][0-9]*)([\+\-]?[0-9]*)$', stripped_message)
    if dice_pattern_match:
        return [_translate_dice_pattern_match(dice_pattern_match)]

    dice_pattern_inverse_match = re.match(r'^([\+\-]?[0-9]+)[\+]([1-9][0-9]*)?[dw]([1-9][0-9]*)$', stripped_message)
    if dice_pattern_inverse_match:
        return [_translate_dice_pattern_inverse_match(dice_pattern_inverse_match)]

    # stop condition for recursion
    if ' ' not in stripped_message:
        raise ValueError

    pattern_splits = stripped_message.split()
    results = []
    for split in pattern_splits:
        results += parse_roll(split)
    return results


def parse_stats(message: str) -> int:
    dice_type_match = re.match(r'^[dw]([1-9][0-9]*)$', message.lstrip().rstrip())
    if dice_type_match:
        return int(dice_type_match.group(1))
    raise ValueError
