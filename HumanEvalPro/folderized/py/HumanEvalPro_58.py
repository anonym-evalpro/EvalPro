from typing import List


def common(l1: List[int], l2: List[int]) -> List[int]:
    """
    Return sorted unique common elements for two integer lists.
    
    Examples:
        >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
        [1, 5, 653]
        >>> common([5, 3, 2, 8], [3, 2])
        [2, 3]
    """
    ret = set()
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                ret.add(e1)
    return sorted(list(ret))


def check(candidate):
    assert candidate([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]
    assert candidate([5, 3, 2, 8], [3, 2]) == [2, 3]
    assert candidate([4, 3, 2, 8], [3, 2, 4]) == [2, 3, 4]
    assert candidate([4, 3, 2, 8], []) == []
    assert candidate([], [3, 2, 4]) == []
    assert candidate([], []) == []
    assert candidate([1, 2, 3], [4, 5, 6]) == []
    assert candidate([-3, -5, -1, 0], [-3, 5, 1, 0]) == [-3, 0]


def test_check():
    check(common)