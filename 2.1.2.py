from helpers import print_inout
from typing import List


@print_inout
def insertion_sort(a: List[int]) -> List[int]:
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1

        while i >= 0 and a[i] > key:
            a[i + 1], a[i] = a[i], a[i + 1]

            i -= 1
        a[i + 1] = key
    return a


@print_inout
def insertion_sort_desc(a: List[int]) -> List[int]:
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1

        while i >= 0 and a[i] < key:
            a[i + 1], a[i] = a[i], a[i + 1]

            i -= 1
        a[i + 1] = key
    return a


if __name__ == "__main__":
    assert insertion_sort([2, 1, 9, 5, 6, 7, 2]) == [1, 2, 2, 5, 6, 7, 9]
    assert insertion_sort_desc([2, 1, 9, 5, 6, 7, 2]) == [9, 7, 6, 5, 2, 2, 1]
