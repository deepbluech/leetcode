__author__ = 'samsung'
import collections
class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        if len(num) < 2:
            return len(num)
        numhash = {}
        for i in num:
            numhash[i] = 0
        maxl = 1
        for i in numhash:
            if numhash.get(i) == 1:
                continue
            j = i
            length = 1
            while numhash.get(j+1) == 0:
                length += 1
                j += 1
                numhash[j] = 1
            j = i
            while numhash.get(j-1) == 0:
                length += 1
                j -= 1
                numhash[j] = 1
            numhash[i] = 1
            maxl = max(maxl, length)
        return maxl

s = Solution()
print s.longestConsecutive([100, 4, 200, 1, 3, 3, 2])