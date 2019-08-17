def binary_search_recursion(sorted_list: list, search: int, low=0, high=0, flag: bool = True) -> int:
    if flag:
        high = len(sorted_list)
    mid = (low + high)//2
    if low < high:
        if search < sorted_list[mid]:
            return binary_search_recursion(sorted_list, search, 0, mid, False)
        elif search > sorted_list[mid]:
            return binary_search_recursion(sorted_list, search, mid+1, high, False)
        else:
            return mid
    return -1


if __name__ == '__main__':
    lst = [23, 34, 45, 54, 61, 63, 77, 89, 91]
    print(binary_search_recursion(lst, 54))
    print(binary_search_recursion(lst, 67))
