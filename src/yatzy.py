from src.pips import Pips
from itertools import groupby


class Yatzy:
    # No es necesario.
    # Lo mantengo para no romper la interfaz
    # publica de la clase segun los
    # casos test originales.
    def __init__(self, *dice):
        self.dice = list(dice)

    @staticmethod
    def chance(*dice):
        return sum(dice)

    @staticmethod
    def yatzy(*dice):
        if dice.count(dice[0]) != len(dice):
            return 0
        return 50

    @staticmethod
    def n_dice(n, *dice):
        return dice.count(n) * n

    def has_n_dice(self, n):
        return self.n_dice(n, *self.dice)

    @staticmethod
    def n_pairs(n, *dice):
        numbers_occurrence_count = {}
        for die in dice:
            if die not in numbers_occurrence_count:
                numbers_occurrence_count[die] = dice.count(die)

        pairs = list(
            filter(
                lambda die: numbers_occurrence_count[die] >= 2,
                sorted(dice, reverse=True),
            )
        )
        if len(pairs) <= n:
            return 0

        grouped_pairs = list(
            filter(lambda x: len(x) >= 2, [list(pair) for key, pair in groupby(pairs)])
        )
        if n == 1:
            return sum(grouped_pairs[0][:2])
        final_sum = sum([pair[0] * n for pair in grouped_pairs[:n]])
        return final_sum

    @classmethod
    def n_of_a_kind(cls, n, *dice, exactly_n=False):
        pip = cls.__biggest_pip_repeated(dice, n)
        if exactly_n:
            for pip in Pips.reversedValues():
                if dice.count(pip) == n:
                    return pip * n
            return 0
        return pip * n if pip else 0

    @classmethod
    def __biggest_pip_repeated(cls, dice, times):
        pips = cls.__filter_pips_repeated(dice, times)
        return pips[0] if pips else []

    @classmethod
    def __filter_pips_repeated(cls, dice, times):
        return list(filter(lambda pip: dice.count(pip) >= times, Pips.reversedValues()))

    @classmethod
    def straight(cls, pip_set, *dice):
        return cls.chance(*dice) if not Pips.minus(pip_set) - set(dice) else 0

    @classmethod
    def large_straight(cls, *dice):
        return cls.chance(*dice) if not Pips.minus(Pips.ONE) - set(dice) else 0

    @classmethod
    def full_house(cls, *dice):
        two_of_a_kind = cls.n_of_a_kind(Pips.TWO.value, *dice, exactly_n=True)
        three_of_a_kind = cls.n_of_a_kind(Pips.THREE.value, *dice)
        if two_of_a_kind and three_of_a_kind:
            return two_of_a_kind + three_of_a_kind
        return 0
