from stack_lp import Stack

def divide_by_two(num):
    """Convert int to bin by / by 2 and keep remainder, rev resulting string"""

    binary = []
    while num > 0:
        rem = num %2
        binary.append(str(rem))
        num = num // 2
    binary.reverse()
    return "".join(binary)

# print(divide_by_two(242))

def convert_to_binary(num):
    """Same as divide by two, but uses Stack class """

    s = Stack()
    bin_rep = ""

    while num > 0:
        rem = num % 2
        s.push(str(rem))
        num = num // 2

    while not s.is_empty():
        bin_rep += s.pop()
    return bin_rep

print(convert_to_binary(242))