def correct_bracketing(brackets: str) -> bool:
    """
    brackets is a string of "<" and ">".
    Check if every opening bracket has a corresponding closing bracket.

    Examples:
        >>> correct_bracketing("<")
        False
        >>> correct_bracketing("<>")
        True
        >>> correct_bracketing("<<><>>")
        True
        >>> correct_bracketing("><<>")
        False
    """
    depth = 0
    for b in brackets:
        if b == "<":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0


def check(candidate):
    assert candidate("") == True
    assert candidate("<>") == True
    assert candidate("<<><>>") == True
    assert candidate("<><><<><>><>") == True
    assert candidate("<><><<<><><>><>><<><><<>>>") == True
    assert candidate("<<<><>>>>") == False
    assert candidate("><<>") == False
    assert candidate("<") == False
    assert candidate("<<<<") == False
    assert candidate(">") == False
    assert candidate("<<>") == False
    assert candidate("<><><<><>><>><<>") == False
    assert candidate("<><><<><>><>>><>") == False


def test_check():
    check(correct_bracketing)