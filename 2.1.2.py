def insertion_sort(a):
    print('Input: insertion_sort({})'.format(a))
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1

        while i >= 0 and a[i] > key:
            a[i+1], a[i] = a[i], a[i+1]

            i = i - 1
        a[i+1] = key

    print('Output: {}\n'.format(a))
    return a


def insertion_sort_desc(a):
    print('Input: insertion_sort_desc({})'.format(a))
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1

        while i >= 0 and a[i] < key:
            a[i+1], a[i] = a[i], a[i+1]

            i = i - 1
        a[i+1] = key

    print('Output: {}\n'.format(a))
    return a

if __name__ == "__main__":
    insertion_sort([2, 1, 9, 5, 6, 7, 2])
    insertion_sort_desc([2, 1, 9, 5, 6, 7, 2])
