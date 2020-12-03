import pytest

# TODO Complete test to validate form data
from app.products.utils import sum_numbers


def test_form_should_throw_error_when_not_valid_data():
    pass


@pytest.mark.parametrize(['test_x', 'test_y', 'expected'], [(1, 2, 3),
                         ("1", 2, 0)])
def test_sum_numbers(test_x, test_y, expected):
    result = sum_numbers(test_x, test_y)
    assert result == expected
