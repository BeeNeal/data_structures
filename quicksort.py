import random
def quicksort(lst):
    """Sort a list using recursive quicksort algorithm.

    >>> quicksort([1, 4, 3, 7, 5])
    [1, 3, 4, 5, 7]

    """

    if len(lst) < 1:
        return lst
    pivot = random.choice(lst)
    high, eq, low = [], [], []
    for item in lst:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            eq.append(item)
        else:
            high.append(item)
    return quicksort(low) + eq + quicksort(high)

# Output random list 
lst = []
counter = 8
while counter:
    lst.append(random.randint(1, 15))
    counter -= 1
print(lst)
print(quicksort(lst))

if __name__ == "__main__":
    import doctest
    if doctest.testmod():
        print("Wow, that was QUICK!")