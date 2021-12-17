import pytest
from hours_to_santa.digits_helper import extract_digits

@pytest.mark.parametrize('n, dp_pos, digits', [
    (0.0024, 0, [0, 0, 0, 2]),
    (0.0025, 0, [0, 0, 0, 3]),
    (0.0324, 0, [0, 0, 3, 2]),
    (0.0325, 0, [0, 0, 3, 3]),
    (0.4324, 0, [0, 4, 3, 2]),
    (0.4325, 0, [0, 4, 3, 3]),
    (5.4324, 0, [5, 4, 3, 2]),
    (5.4325, 0, [5, 4, 3, 3]),
    (54.324, 1, [5, 4, 3, 2]),
    (54.325, 1, [5, 4, 3, 3]),
    (543.24, 2, [5, 4, 3, 2]),
    (543.25, 2, [5, 4, 3, 3]),
    (5432.4, 3, [5, 4, 3, 2]),
    (5432.5, 3, [5, 4, 3, 3]),
    (999.95, 3, [1, 0, 0, 0]),
])
def test_extract_very_low(n, dp_pos, digits):
    extracted = extract_digits(n)
    assert extracted['dp_pos'] == dp_pos
    assert extracted['digits'] == digits
