from typing import Iterable, Set
from itertools import groupby
from src.pips import Pips


class Yatzy:
    # No es necesario.
    # Lo mantengo para no romper la interfaz
    # publica de la clase segun los
    # casos test originales.
    def __init__(self, *dice: Iterable[int]):
        self.dice = dice

    @staticmethod
    def chance(*dice: Iterable[int]) -> int:
        return sum(dice)

    @staticmethod
    def yatzy(*dice: Iterable[int]) -> int:
        NO_SCORE = 0
        FIFTY_SCORE = 50
        if dice.count(dice[0]) != len(dice):
            return NO_SCORE
        return FIFTY_SCORE

    @staticmethod
    def __n_dice(pip: Pips, *dice: Iterable[int]) -> int:
        n = pip.value
        return dice.count(n) * n

    @classmethod
    def ones(cls, *dice: Iterable[int]) -> int:
        return cls.__n_dice(Pips.ONE, *dice)

    @classmethod
    def twos(cls, *dice: Iterable[int]) -> int:
        return cls.__n_dice(Pips.TWO, *dice)

    @classmethod
    def threes(cls, *dice: Iterable[int]) -> int:
        return cls.__n_dice(Pips.THREE, *dice)

    @classmethod
    def fours(cls, *dice: Iterable[int]) -> int:
        return cls.__n_dice(Pips.FOUR, *dice)

    @classmethod
    def fives(cls, *dice: Iterable[int]) -> int:
        return cls.__n_dice(Pips.FIVE, *dice)

    @classmethod
    def sixes(cls, *dice: Iterable[int]) -> int:
        return cls.__n_dice(Pips.SIX, *dice)

    def has_n_dice(self, pip: Pips) -> int:
        return self.__n_dice(pip, *self.dice)

    @staticmethod
    def __n_pairs(number_of_pairs: int, *dice: Iterable[int]) -> int:
        PAIR = 2

        pairs = sorted(
            filter(
                lambda die: dice.count(die) >= PAIR,
                dice,
            ),
            reverse=True,
        )

        if len(pairs) <= number_of_pairs:
            return 0

        grouped_pairs = tuple(groupby(pairs))
        return sum(map(lambda x: x[0] * PAIR, grouped_pairs[:number_of_pairs]))

    @classmethod
    def pair(cls, *dice: Iterable[int]) -> int:
        ONE_PAIR = Pips.ONE.value
        return cls.__n_pairs(ONE_PAIR, *dice)

    @classmethod
    def two_pairs(cls, *dice: Iterable[int]) -> int:
        TWO_PAIRS = Pips.TWO.value
        return cls.__n_pairs(TWO_PAIRS, *dice)

    @classmethod
    def __n_of_a_kind(
        cls, n: int, *dice: Iterable[int], exactly_n: bool = False
    ) -> int:
        if exactly_n:
            for pip in reversed(Pips):
                if dice.count(pip.value) == n:
                    return pip.value * n
            return 0
        biggest_pip = cls.__biggest_pip_repeated(dice, n)
        return biggest_pip.value * n if biggest_pip else 0

    @classmethod
    def two_of_a_kind(cls, *dice: Iterable[int]) -> int:
        return cls.__n_of_a_kind(Pips.TWO.value, *dice, exactly_n=True)

    @classmethod
    def three_of_a_kind(cls, *dice: Iterable[int]) -> int:
        return cls.__n_of_a_kind(Pips.THREE.value, *dice)

    @classmethod
    def four_of_a_kind(cls, *dice: Iterable[int]) -> int:
        return cls.__n_of_a_kind(Pips.FOUR.value, *dice)

    @classmethod
    def __filter_pips_repeated(cls, dice: Iterable[int], times: int) -> Set[Pips]:
        return set(filter(lambda pip: dice.count(pip.value) >= times, Pips))

    @classmethod
    def __biggest_pip_repeated(cls, dice: Iterable[int], times: int) -> Pips:
        pips = cls.__filter_pips_repeated(dice, times)
        return max(pips) if pips else 0

    @classmethod
    def __straight(cls, pip: Pips, *dice: Iterable[int]) -> int:
        return cls.chance(*dice) if not Pips.exclude_values(pip) - set(dice) else 0

    @classmethod
    def small_straight(cls, *dice: Iterable[int]) -> int:
        return cls.__straight(Pips.SIX, *dice)

    @classmethod
    def large_straight(cls, *dice: Iterable[int]) -> int:
        return cls.__straight(Pips.ONE, *dice)

    @classmethod
    def full_house(cls, *dice: Iterable[int]) -> int:
        two_of_a_kind = cls.two_of_a_kind(*dice)
        three_of_a_kind = cls.three_of_a_kind(*dice)
        if two_of_a_kind and three_of_a_kind:
            return two_of_a_kind + three_of_a_kind
        return 0
