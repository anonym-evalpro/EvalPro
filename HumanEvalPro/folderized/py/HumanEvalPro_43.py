from typing import List


def pairs_sum_to_zero(l: List[int]) -> bool:
    """
    Check if there are two distinct elements
    in the list that sum to zero.
    
    Examples:
        >>> pairs_sum_to_zero([1, 3, 5, 0])
        False
        >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
        True
    """
    for i, l1 in enumerate(l):
        for j in range(i + 1, len(l)):
            if l1 + l[j] == 0:
                return True
    return False


def check(candidate):
    assert candidate([1, 3, 5, 0]) == False
    assert candidate([1, 3, -2, 1]) == False
    assert candidate([1, 2, 3, 7]) == False
    assert candidate([2, 4, -5, 3, 5, 7]) == True
    assert candidate([1]) == False
    assert candidate([]) == False
    assert candidate([0, 0]) == True

    assert candidate([-3, 9, -1, 3, 2, 30]) == True
    assert candidate([-3, 9, -1, 3, 2, 31]) == True
    assert candidate([-3, 9, -1, 4, 2, 30]) == False
    assert candidate([-3, 9, -1, 4, 2, 31]) == False


def test_check():
    check(pairs_sum_to_zero)