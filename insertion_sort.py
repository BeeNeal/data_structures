def insertion_sort(lst):
    """iterate through list putting each item in correct place through series of swaps
    Use on already partially sorted lists no more than 10,000 items

    >>> insertion_sort([1, 4, 3, 7, 5])
    [1, 3, 4, 5, 7]
     """
    for i in range(1, len(lst)):
        # save this assignment so do less operations per swap
        curr = lst[i]
        j = i # remember curr's index
        # go backward through the list, starting wherever i left off
        # starts at 0, stops at 0, goes backwards, so shouldn't have index out of range issue
        # starting at higher end, move all values forward until elem in correct spot in list

        while j >= 1 and curr < lst[j - 1]:
            lst[j] = lst[j - 1]
            j -= 1

        #    put it in the right place
        lst[j] = curr
    return lst