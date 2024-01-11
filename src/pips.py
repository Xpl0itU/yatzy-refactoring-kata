from enum import Enum, unique


@unique
class Pips(Enum):
    ONE, TWO, THREE, FOUR, FIVE, SIX = range(1, 6 + 1)

    @classmethod
    def values(cls, *values_to_exclude):
        for number in Pips.__members__.values():
            if number not in values_to_exclude:
                yield number.value
