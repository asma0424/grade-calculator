
import pytest
from calculator import calculate_average, is_passing, get_grade


def test_calculate_average():
    assert calculate_average([10, 12, 14]) == 12


def test_is_passing():
    assert is_passing(12) is True
    assert is_passing(8) is False


def test_empty_grades():
    with pytest.raises(ValueError):
        calculate_average([])


def test_grade_classification():
    assert get_grade(18) == "A"
    assert get_grade(15) == "B"
    assert get_grade(12) == "C"
    assert get_grade(10) == "D"
    assert get_grade(7) == "F"


def test_invalid_average():
    with pytest.raises(ValueError):
        get_grade(-1)

    with pytest.raises(ValueError):
        get_grade(21)
