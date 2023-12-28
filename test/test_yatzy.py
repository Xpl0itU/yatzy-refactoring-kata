from src.pips import Pips
from src.yatzy import Yatzy

# Casos test iniciales del kata para refactorizar
# No lanzarlos contra mi solucion.


def test_chance_scores_sum_of_all_dice():
    expected = 15
    actual = Yatzy.chance(2, 3, 4, 5, 1)
    assert expected == actual
    assert 16 == Yatzy.chance(3, 3, 4, 5, 1)


def test_yatzy_scores_50():
    expected = 50
    actual = Yatzy.yatzy(4, 4, 4, 4, 4)
    assert expected == actual
    assert 50 == Yatzy.yatzy(6, 6, 6, 6, 6)
    assert 0 == Yatzy.yatzy(6, 6, 6, 6, 3)


def test_1s():
    assert Yatzy.n_dice(Pips.ONE.value, 1, 2, 3, 4, 5) == 1
    assert 2 == Yatzy.n_dice(Pips.ONE.value, 1, 2, 1, 4, 5)
    assert 0 == Yatzy.n_dice(Pips.ONE.value, 6, 2, 2, 4, 5)
    assert 4 == Yatzy.n_dice(Pips.ONE.value, 1, 2, 1, 1, 1)


def test_2s():
    assert 4 == Yatzy.n_dice(Pips.TWO.value, 1, 2, 3, 2, 6)
    assert 10 == Yatzy.n_dice(Pips.TWO.value, 2, 2, 2, 2, 2)


def test_threes():
    assert 6 == Yatzy.n_dice(Pips.THREE.value, 1, 2, 3, 2, 3)
    assert 12 == Yatzy.n_dice(Pips.THREE.value, 2, 3, 3, 3, 3)


def test_fours_test():
    assert 12 == Yatzy.n_dice(Pips.FOUR.value, 4, 4, 4, 5, 5)
    assert 8 == Yatzy.n_dice(Pips.FOUR.value, 4, 4, 5, 5, 5)
    assert 4 == Yatzy.n_dice(Pips.FOUR.value, 4, 5, 5, 5, 5)


def test_fives():
    assert 10 == Yatzy.n_dice(Pips.FIVE.value, 4, 4, 4, 5, 5)
    assert 15 == Yatzy.n_dice(Pips.FIVE.value, 4, 4, 5, 5, 5)
    assert 20 == Yatzy.n_dice(Pips.FIVE.value, 4, 5, 5, 5, 5)


def test_sixes_test():
    assert 0 == Yatzy.n_dice(Pips.SIX.value, 4, 4, 4, 5, 5)
    assert 6 == Yatzy.n_dice(Pips.SIX.value, 4, 4, 6, 5, 5)
    assert 18 == Yatzy.n_dice(Pips.SIX.value, 6, 5, 6, 6, 5)


def test_one_pair():
    assert 6 == Yatzy.n_pairs(Pips.ONE.value, 3, 4, 3, 5, 6)
    assert 10 == Yatzy.n_pairs(Pips.ONE.value, 5, 3, 3, 3, 5)
    assert 12 == Yatzy.n_pairs(Pips.ONE.value, 5, 3, 6, 6, 5)


def test_two_Pair():
    assert 16 == Yatzy.n_pairs(Pips.TWO.value, 3, 3, 5, 4, 5)
    assert 18 == Yatzy.n_pairs(Pips.TWO.value, 3, 3, 6, 6, 6)
    assert 0 == Yatzy.n_pairs(Pips.TWO.value, 3, 3, 6, 5, 4)


def test_three_of_a_kind():
    assert 9 == Yatzy.n_of_a_kind(Pips.THREE.value, 3, 3, 3, 4, 5)
    assert 15 == Yatzy.n_of_a_kind(Pips.THREE.value, 5, 3, 5, 4, 5)
    assert 9 == Yatzy.n_of_a_kind(Pips.THREE.value, 3, 3, 3, 3, 5)


def test_four_of_a_knd():
    assert 12 == Yatzy.n_of_a_kind(Pips.FOUR.value, 3, 3, 3, 3, 5)
    assert 20 == Yatzy.n_of_a_kind(Pips.FOUR.value, 5, 5, 5, 4, 5)
    assert 12 == Yatzy.n_of_a_kind(Pips.FOUR.value, 3, 3, 3, 3, 3)
    assert 0 == Yatzy.n_of_a_kind(Pips.FOUR.value, 3, 3, 3, 2, 1)


def test_smallStraight():
    assert 15 == Yatzy.small_straight(1, 2, 3, 4, 5)
    assert 15 == Yatzy.small_straight(2, 3, 4, 5, 1)
    assert 0 == Yatzy.small_straight(1, 2, 2, 4, 5)


def test_largeStraight():
    assert 20 == Yatzy.large_straight(6, 2, 3, 4, 5)
    assert 20 == Yatzy.large_straight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.large_straight(1, 2, 2, 4, 5)


def test_fullHouse():
    assert 18 == Yatzy.fullHouse(6, 2, 2, 2, 6)
    assert 0 == Yatzy.fullHouse(2, 3, 4, 5, 6)
