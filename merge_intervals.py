def merge_intervals(intervals):
    """Given a list of intervals, merge all overlapping intervals

    >>> merge_intervals([[1,3],[2,6],[8,10],[15,18]])
    [[1, 6], [8, 10], [15, 18]]
    >>> merge_intervals([[1,4],[4,5], [5, 6]])
    [[1, 6]]
    >>> merge_intervals([[1,4],[0,4]])
    [[0, 4]]
    >>> merge_intervals([])
    []
    """

    if len(intervals) < 1:
        return intervals

    j = 1
    intervals.sort()
    merged = [intervals[0]]

    while j < len(intervals):
        if intervals[j][0] in range(merged[-1][0], merged[-1][1] + 1):
            # use max to account for intervals inside ie: [1, 5][3, 4]
            merged[-1] = [merged[-1][0], max(intervals[j][1], merged[-1][1])]
            j += 1
        else:
            merged.append(intervals[j])
            j += 1
    return merged


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\ninterBALLIN'!")