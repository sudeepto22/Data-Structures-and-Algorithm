def binary_search(sorted_array: list, search: int) -> int:
    """
    Binary Search Algorithm

    Time Complexity --> O(Log N)

    :param sorted_array: list
    :param search: int

    :return index: int
    """
    low = 0
    high = len(sorted_array)

    while low < high:
        mid = (low + high) // 2

        if search < sorted_array[mid]:
            high = mid
        elif search > sorted_array[mid]:
            low = mid + 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    lst = [23, 34, 45, 54, 61, 63, 77, 89, 91]
    print(binary_search(lst, 54))
    print(binary_search(lst, 67))
