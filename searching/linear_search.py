def linear_search(nums_array: list, search: int) -> int:
    """
    Linear Search Algorithm

    Time Complexity --> O(N)

    :param nums_array: list
    :param search: int

    :return index: int
    """
    for i in range(len(nums_array)):
        if search == nums_array[i]:
            return i
    return -1


if __name__ == '__main__':
    lst = [54, 23, 45, 12, 37, 89, 21]
    print(linear_search(lst, 37))
    print(linear_search(lst, 13))
