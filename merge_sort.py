# split the input in half
# sort each half by recursively using this same process
# merge the sorted halves back together

def mergesort(lst):
    """Sorts list in place using merge sort O(nlogn)"""
    if len(lst) > 1:
        mid = len(lst) // 2
        l = lst[:mid]
        r = lst[mid:]
        mergesort(l)
        mergesort(r)

        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                lst[k] = l[i]
                i += 1
            else:
                lst[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            lst[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            lst[k] = r[j]
            j += 1
            k += 1           

    return lst

print(mergesort([1, 9, 4, 8, 3, 4, 3, 6, 7]))