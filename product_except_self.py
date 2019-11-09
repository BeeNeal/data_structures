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

if __name__ == "__main__":
    import doctest
    if doctest.testmod():
        print("Yahooo!")