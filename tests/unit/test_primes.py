import pytest
from src.algorithms.primes import is_prime, get_primes

pytestmark = pytest.mark.unit


def test__is_prime__returns_true():
    # Act
    result = is_prime(5)

    # Assert
    assert result is True


def test__is_prime__returns_false():
    result = is_prime(10)
    assert (result is False)


def test__get_primes__4_first_primes():
    result = get_primes(4)
    assert result == [2, 3, 5, 7]
