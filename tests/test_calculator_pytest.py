import pytest
from calculator import calculator


def test_plus():
    assert calculator('5+4') == 9


def test_no_signs():
    with pytest.raises(ValueError) as error:
        calculator('3 6')
    assert 'Выражение должно содержать один знак из (+-/*)' == error.value.args[0]


def test_two_signs():
    with pytest.raises(ValueError) as error:
        calculator('3 - 6 /')
    assert 'Выражение должно содержать два целых числа и один знак' == error.value.args[0]


if __name__ == '__main__':
    pytest.main()
