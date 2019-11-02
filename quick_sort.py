import random
def quicksort(lst):
    """ """

    # base case for the recursive call that will order them back up the call stack
    if len(lst) < 2:
        return lst

    pivot = random.choice(lst)
    low, eq, high = [], [], []
    for item in lst:
        if item < pivot:
            low.append(item)
        elif item > pivot:
            high.append(item)
        else:
            eq.append(item)
    return quicksort(low) + eq + quicksort(high)

print(quicksort([1, 9, 4, 8, 3, 4, 3, 6, 7]))