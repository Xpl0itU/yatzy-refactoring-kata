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
        score = 0
        for die in dice:
            score += die
        return score

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
    def three_of_a_kind(cls, *dice):
        THREE = 3
        pip = cls.__biggest_pip_repeated(dice, THREE)
        return pip * THREE if pip else 0

    @classmethod
    def four_of_a_kind(cls, *dice):
        FOUR = 4
        pip = cls.__biggest_pip_repeated(dice, FOUR)
        return pip * FOUR if pip else 0

    @classmethod
    def __biggest_pip_repeated(cls, dice, times):
        pips = cls.__filter_pips_repeated(dice, times)
        return pips[0] if pips else []

    @classmethod
    def __filter_pips_repeated(cls, dice, times):
        return list(filter(lambda pip: dice.count(pip) >= times, Pips.reversedValues()))

    @classmethod
    def small_straight(cls, *dice):
        return cls.chance(*dice) if not Pips.minus(Pips.SIX) - set(dice) else 0

    @classmethod
    def large_straight(cls, *dice):
        return cls.chance(*dice) if not Pips.minus(Pips.ONE) - set(dice) else 0

    @classmethod
    def fullHouse(cls, *dice):
        if cls.two_of_a_kind(*dice) and cls.three_of_a_kind(*dice):
            return cls.two_of_a_kind(*dice) + cls.three_of_a_kind(*dice)
        else:
            return 0

    @classmethod
    def two_of_a_kind(cls, *dice):
        PAIR = 2
        for pip in Pips.reversedValues():
            if dice.count(pip) == PAIR:
                return PAIR * pip
        return 0
