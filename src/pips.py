from enum import Enum, unique
from typing import List, Iterable, Set


@unique
class Pips(Enum):
    ONE, TWO, THREE, FOUR, FIVE, SIX = range(1, 6 + 1)

    @classmethod
    def values(cls) -> List[int]:
        return [number._value_ for number in Pips.__members__.values()]

    @classmethod
    def reversedValues(cls) -> Iterable[int]:
        return reversed(cls.values())

    @classmethod
    def minus(cls, pip) -> Set[int]:
        return set(cls.values()) - {pip.value}
