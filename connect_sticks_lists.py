
# Problem description: 
# You have some sticks with positive integer lengths.

# You can connect any two sticks of lengths X and Y into one stick by paying a
#  cost of X + Y.  You perform this action until there is one stick remaining.

# Return the min cost of connecting all the sticks into one stick in this way.

sticks = [3354,4316,3259,4904,4598,474,3166,6322,8080,9009]

import heapq

def connect_sticks_heap(sticks):
    """GOOD SOLUTION - Return total cost of connecting sticks using min heap."""
    
    total_cost = 0

    # turn input list into a heap
    heapq.heapify(sticks)
    i = len(sticks) - 1
    while i >= 1:
        combined_stick = heapq.heappop(sticks) + heapq.heappop(sticks)
        total_cost += combined_stick
        heapq.heappush(sticks, combined_stick)
        i -= 1
    return total_cost

print(connect_sticks_heap(sticks))


def connectSticks(sticks):
    """BAD SOLUTION """

    total_cost = 0
    sticks.sort(reverse=True)
    i = len(sticks) - 1
    while i >= 1:
        combined_stick = sticks.pop() + sticks.pop()
        total_cost += combined_stick
        sticks.append(combined_stick)
        i -= 1
    return total_cost

# connectSticks doesn't work, because with longer lists, we need to resort, or 
# else the combined_stick that is getting appended becomes greater than a stick 
# in the list, and so we are no longer adding together the smallest sticks.
# solution? Similary strategy, but use min heap, so can put sticks in the
# correct order and always add smallest sticks.

# print(connectSticks([2,4,3]))
# 14