def get_max_subarray_sum(nums_array: list) -> int:
    """
    Algorithm for getting the maximum sum of a subarray (Kadane's Algorithm)

    Complexity --> O(N)

    :param nums_array: list
    :return sum: int
    """
    global_sum = local_sum = nums_array[0]
    for i in range(1, len(nums_array)):
        if local_sum + nums_array[i] > nums_array[i]:
            local_sum += nums_array[i]
        else:
            local_sum = nums_array[i]
        if local_sum > global_sum:
            global_sum = local_sum
    return global_sum


if __name__ == '__main__':
    lst = [1, -2, 4, -1, 6, -5, 6]
    print(get_max_subarray_sum(lst))
