def bubble_sort(nums_array):
    is_sorted = True
    for i in range(0, len(nums_array)-1):
        for j in range(0, len(nums_array)-i-1):
            if nums_array[j] > nums_array[j+1]:
                is_sorted = False
                temp = nums_array[j]
                nums_array[j] = nums_array[j+1]
                nums_array[j+1] = temp
            print(nums_array)
        if is_sorted:
            break
        print()

    return nums_array


lst = [54, 23, 45, 12, 37, 89, 21]
print(bubble_sort(lst))

