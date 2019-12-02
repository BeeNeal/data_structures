# ways to traverse lists

def print_list_in_reverse(lst):
    i = len(lst) - 1
    while i >= 0:
        print(lst[i])
        i -= 1
print_list_in_reverse([1, 2, 3])