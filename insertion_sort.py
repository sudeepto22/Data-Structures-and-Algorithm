def insertion_sort(nums_array):
    for i in range(1, len(nums_array)):
        n = nums_array[i]
        index = i - 1
        while index >= 0 and nums_array[index] > n:
            nums_array[index + 1] = nums_array[index]
            index -= 1
        nums_array[index + 1] = n
    return nums_array


lst = [54, 23, 45, 12, 37, 89, 21]
print(insertion_sort(lst))
