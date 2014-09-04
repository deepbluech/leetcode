__author__ = 'Administrator'
class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        if len(A) == 0:
            return False
        if len(A) == 1:
            if A[0] == target:
                return True
            else:
                return False

        l = 0
        r = len(A) - 1
        while l <= r:
            mid = l + (r - l) / 2
            if A[mid] == target:
                return True
            if A[mid] > A[r]:
                #left ordered
                if target >= A[l] and target < A[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif A[mid] < A[r]:
                #right ordered
                if target > A[mid] and target <= A[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                    r -= 1
        return False

so = Solution()
print so.search([1,0,1,1,1], 0)