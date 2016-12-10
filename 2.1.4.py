def binary_add(a, b):
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

if __name__ == "__main__":
    binary_add([1, 0, 1, 1], [1, 1, 1, 0])
