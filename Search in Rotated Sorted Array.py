__author__ = 'Administrator'
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        n = len(A)
        if n == 0:
            return -1
        if n == 1:
            if A[0] == target:
                return 0
            else:
                return -1
        if A[n-1] > A[0]:
            return self.binary_search(A, target, 0, n-1)

        break_idx = self.find_break_index(A, 0, n-1)
        print break_idx
        largest_val = A[break_idx - 1]
        smallest_val = A[break_idx]
        head_val = A[0]
        tail_val = A[n-1]

        if target >= smallest_val and target <= tail_val:
            return self.binary_search(A, target, break_idx, n-1)
        if target >= head_val and target <= largest_val:
            return self.binary_search(A, target, 0, break_idx)
        return -1

    def find_break_index(self, A, start, end):
        if end - start == 1:
            return end
        if end - start == 0:
            return -1
        mid = start + (end - start) / 2
        while A[mid] > A[start]:
            start = mid
            mid = (mid + 1 + end) / 2
        return self.find_break_index(A, start, mid)

    def binary_search(self, A, target, start, end):
        if start > end or start < 0 or end >= len(A):
            return -1
        mid = start + (end - start) / 2
        if A[mid] == target:
            return mid
        elif A[mid] < target:
            return self.binary_search(A, target, mid+1, end)
        else:
            return self.binary_search(A, target, start, mid-1)

if __name__ == '__main__':
    s = Solution()
    #no duplicate
    A = [1,1,1,0,1]
    print s.find_break_index(A, 0, len(A)-1)