from enum import IntEnum, unique


@unique
class Pips(IntEnum):
    ONE, TWO, THREE, FOUR, FIVE, SIX = range(1, 6 + 1)

    @classmethod
    def exclude_values(cls, *values_to_exclude):
        return set(filter(lambda pip: pip not in values_to_exclude, Pips))
