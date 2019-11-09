import numpy
# this solution works for small lists, but has poor runtime
def productExceptSelf(nums):
    """
    >>> productExceptSelf([1,2,3,4])
    [24, 12, 8, 6]

    """
        
    output = []
    for i in range(len(nums)):
        prod = numpy.prod(nums[i+1:]) * numpy.prod(nums[:i])
        output.append(int(prod))
    return output

nums = [1,2,3,4]
result = 1
for item in nums:
    result *= item
print(result)
# thoughts:
#         keep a running total of product of all items left to pointer
# start from reverse?

#         get the product from reverse(j)
# store the product from the front, mult together with item from back
# for good space complexity, once saved i val, replace it in list with i * j val
# won't have all of the products until have gone all the way through j
        
#         l_prod = None
#         r_prod = None
#         i = 0
#         j = len(nums) -1
#         while j > 0 and i < len(nums):

def productExceptSelf(self, nums: List[int]) -> List[int]:

    # The length of the input array 
    length = len(nums)

    # The answer array to be returned
    answer = [0]*length

    # answer[i] contains the product of all the elements to the left
    # Note: for the element at index '0', there are no elements to the left,
    # so the answer[0] would be 1
    answer[0] = 1
    for i in range(1, length):
        
        # answer[i - 1] already contains the product of elements to the left of 'i - 1'
        # Simply multiplying it with nums[i - 1] would give the product of all 
        # elements to the left of index 'i'
        answer[i] = nums[i - 1] * answer[i - 1]

    # R contains the product of all the elements to the right
    # Note: for the element at index 'length - 1', there are no elements to the right,
    # so the R would be 1
    R = 1;
    for i in reversed(range(length)):
        
        # For the index 'i', R would contain the 
        # product of all elements to the right. We update R accordingly
        answer[i] = answer[i] * R
        R *= nums[i]

    return answer

if __name__ == "__main__":
    import doctest
    if doctest.testmod():
        print("Yahooo!")