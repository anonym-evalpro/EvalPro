from typing import List


def derivative(xs: List[int]) -> List[int]:
    """
    xs represents the coefficients of a polynomial:
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
    Return the derivative of this polynomial in the same form.
    
    Examples:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
        >>> derivative([1, 2, 3])
        [2, 6]
    """
    return [(i * x) for i, x in enumerate(xs)][1:]


def check(candidate):
    assert candidate([]) == []
    assert candidate([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert candidate([1, 2, 3]) == [2, 6]
    assert candidate([3, 2, 1]) == [2, 2]
    assert candidate([3, 2, 1, 0, 4]) == [2, 2, 0, 16]
    assert candidate([1]) == []
    assert candidate([4, -2, -1, -3, -5]) == [-2, -2, -9, -20]


def test_check():
    check(derivative)