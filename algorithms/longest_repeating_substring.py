def get_longest_repeating_substring(input_string: str) -> str:
    """
    Algorithm for getting the longest repeating substring from a string

    Complexity --> O(N)

    :param input_string: str

    :return longest_substring: str
    """
    longest_substring = ""
    local_longest_substring = input_string[0]

    for i in range(1, len(input_string)):
        if local_longest_substring[0] == input_string[i]:
            local_longest_substring += input_string[i]
        else:
            local_longest_substring = input_string[i]

        if len(local_longest_substring) > len(longest_substring):
            longest_substring = local_longest_substring
    return longest_substring


if __name__ == '__main__':
    inp_string = "aabcccddddee"
    print(get_longest_repeating_substring(inp_string))
