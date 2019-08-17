def selection_sort(nums_array: list) -> list:
    """
    Selection Sort Algorithm
    :param nums_array: list
    :return nums_array: list
    """
    for i in range(len(nums_array)):
        min_index = i
        for j in range(i + 1, len(nums_array)):
            if nums_array[j] < nums_array[min_index]:
                min_index = j
        if min_index != i:
            temp = nums_array[i]
            nums_array[i] = nums_array[min_index]
            nums_array[min_index] = temp
    return nums_array


if __name__ == '__main__':
    lst = [12, 23, 45, 12, 37, 89, 99]
    print(selection_sort(lst))
