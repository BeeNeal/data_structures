class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if self.is_monotonic_increasing(A):
            return True
        elif self.is_monotonic_decreasing(A):
            return True
        return False
            
    def is_monotonic_increasing(self, A):
        i = 0
        j = 1
        while j < len(A):
            # for ind, val in enumerate(A):
            if A[i] <= A[j]:
                i += 1
                j += 1
                continue

            else:
                return False
        return True
                    
        
    def is_monotonic_decreasing(self, A):
        i = 0
        j = 1
        while j < len(A):
            # for ind, val in enumerate(A):
            if A[i] >= A[j]:
                i += 1
                j += 1
                continue
            else:
                return False
        return True

A = [1,2,2,3]
B = [6,5,4,4]
C = [1,3,2]
x = Solution()
print(x.isMonotonic(A))
print(x.isMonotonic(B))
print(x.isMonotonic(C))