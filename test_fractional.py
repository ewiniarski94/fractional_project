import pytest
from fractional import Fractional

class TestFractional:

    def test_add(self):
        f1 = Fractional(1, 2)
        f2 = Fractional(1, 3)
        result = f1 + f2
        expected = Fractional(5, 6) 
        assert result == expected

    def test_sub(self):
        f1 = Fractional(3, 4)
        f2 = Fractional(1, 4)
        result = f1 - f2 
        expected = Fractional(8, 16)
        assert result == expected

    def test_mul(self):
        f1 = Fractional(2, 3)
        f2 = Fractional(3, 5)
        result = f1 * f2
        expected = Fractional(6, 15)
        assert result == expected

    def test_div(self):
        f1 = Fractional(1, 2)
        f2 = Fractional(2, 3)
        result = f1 / f2
        expected = Fractional(3, 4)
        assert result == expected

    def test_eq(self):
        f1 = Fractional(1, 2)
        f2 = Fractional(2, 4)
        assert f1 == f2

    def test_eq_negative(self):
        f1 = Fractional(1, 2)
        f2 = Fractional(1, 3)
        assert f1 != f2

    def test_lt_lower_than(self):
        assert Fractional(1, 3) < Fractional(1, 2)

    def test_lt_lower_than_negative(self):
        assert not (Fractional(1, 2) < Fractional(1, 3))

    def test_gt_bigger_than(self):
        assert Fractional(1, 2) > Fractional(1, 3)

    def test_gt_bigger_than_negative(self):
        assert not (Fractional(1, 3) > Fractional(1, 2))

    def test_le_lower_or_equal(self):
        assert Fractional(1, 3) <= Fractional(1, 2)
        assert Fractional(1, 2) <= Fractional(2, 4)

    def test_le_lower_or_equal_negative(self):
        assert not (Fractional(1, 2) <= Fractional(1, 3))

    def test_ge_bigger_or_equal(self):
        assert Fractional(1, 2) >= Fractional(1, 3)
        assert Fractional(2, 4) >= Fractional(1, 2)

    def test_ge_bigger_or_equal_negative(self):
        assert not (Fractional(1, 3) >= Fractional(1, 2))