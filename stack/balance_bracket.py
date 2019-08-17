import stack


def is_balanced(input_string: str) -> bool:
    """
    Check if the given string is bracket balanced

    :param input_string: str

    :return is_balanced: bool
    """
    bracket_in = "[{("
    bracket_out = "]})"

    bracket_stack = stack.Stack()

    for i in input_string:
        if i in bracket_in:
            bracket_stack.push(bracket_in.index(i))
        elif i in bracket_out:
            if bracket_stack.top() == bracket_out.index(i):
                bracket_stack.pop()
    if bracket_stack.is_empty():
        return True
    return False


if __name__ == '__main__':
    bracket_string1 = "(hello {world [bracket]})"
    bracket_string2 = "(hello {world [bracket}])"
    print(is_balanced(bracket_string1))
    print(is_balanced(bracket_string2))

