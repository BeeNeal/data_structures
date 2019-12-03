from collections import Counter

def k_frequent_elements(lst, k):
    """Given an array of integers, return the k most frequent elements.
    
    >>> print(k_frequent_elements([1,1,1,2,2,3], 2))
    [1, 2]
    >>> print(k_frequent_elements([3], 1))
    [3]
    """

    cnt = Counter()
    for elem in lst:
        cnt[elem] += 1

    most_frequent = [elem[0] for elem in cnt.most_common(k)]
    # need to sort dictionary by values, but keep the keys
    return most_frequent


if __name__ == "__main__":
    import doctest
    if doctest.testmod():
        print("You are one smart bumblebee!")