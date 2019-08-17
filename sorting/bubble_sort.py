def bubble_sort(nums_array: list) -> list:
    """
    Bubble Sort Algorithm

    :param nums_array: list
    :return nums_array: list
    """
    is_sorted = True
    for i in range(0, len(nums_array) - 1):
        for j in range(0, len(nums_array) - i - 1):
            if nums_array[j] > nums_array[j + 1]:
                is_sorted = False
                temp = nums_array[j]
                nums_array[j] = nums_array[j + 1]
                nums_array[j + 1] = temp
        if is_sorted:
            break

    return nums_array


if __name__ == '__main__':
    lst = [54, 23, 45, 12, 37, 89, 21]
    print(bubble_sort(lst))
