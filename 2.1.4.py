from helpers import print_inout
from typing import List


@print_inout
def binary_add(a: List[int], b: List[int]) -> List[int]:
    c = []

    remainder = 0
    for pair in zip(reversed(a), reversed(b)):
        remainder, val = divmod(sum(pair) + remainder, 2)
        c.append(val)

    c.append(remainder)

    return list(reversed(c))


if __name__ == "__main__":
    assert binary_add([1, 0, 1, 1], [1, 1, 1, 0]) == [1, 1, 0, 0, 1]
    assert binary_add([1, 0], [0, 1]) == [0, 1, 1]
    assert binary_add([0, 1], [0, 1]) == [0, 1, 0]
