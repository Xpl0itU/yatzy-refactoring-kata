from enum import Enum, unique


@unique
class Pips(Enum):
    ONE, TWO, THREE, FOUR, FIVE, SIX = range(1, 6 + 1)

    @classmethod
    def values(cls):
        return [number._value_ for number in Pips.__members__.values()]

    @classmethod
    def reversedValues(cls):
        return reversed(cls.values())

    @classmethod
    def minus(cls, pip):
        return set(cls.values()) - {pip.value}
