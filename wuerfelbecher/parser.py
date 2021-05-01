import re
from collections import namedtuple
from . import dice_roller

SetToRoll = namedtuple('SetToRoll', ['count', 'dice_type', 'modifier'])

def parse_roll(message: str) -> SetToRoll:
    m = re.match(r'^([1-9])?[dw]([0-9]+)([\+\-]?[0-9]*)$', message.lstrip().rstrip())
    if m:
        count = 1 if m.group(1) is None else int(m.group(1))
        dice_type = int(m.group(2))
        modifier = 0 if m.group(3) == '' else int(m.group(3))
        return SetToRoll(count, dice_type, modifier)
    raise ValueError

def parse_stats(message: str) -> int:
    m = re.match(r'^[dw]([0-9]+)$', message.lstrip().rstrip())
    if m:
        return int(m.group(1))
    raise ValueError
