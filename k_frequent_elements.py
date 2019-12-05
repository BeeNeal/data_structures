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

def k_frequent_words(words, k):
    """Return k most frequent words, if k is tied, lowest lexicographical word """

    cnt = collections.Counter()
    for word in words:
        cnt[word] += 1
    most_frequent = [word[0] for word in cnt.most_common(k) ]
    return most_frequent

def k_most_freq(lst, k):
    """same as above, but without using collections library

    >>> print(k_most_freq([1,1,1,2,2,3], 2))
    [1, 2]
    >>> print(k_most_freq([3], 1))
    [3]
    >>> print(k_most_freq([1,1,1,2,2,3, 0, 0, 0, 0], 3))
    [0, 1, 2]
    """
    # if must use dict
    counts = dict()
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    newf = list(counts.items()).sort(reverse=True, key=lambda x: x[1])
    print(newf)
    # return newf


if __name__ == "__main__":
    import doctest
    if not doctest.testmod():
        print("You are one smart bumblebee!")