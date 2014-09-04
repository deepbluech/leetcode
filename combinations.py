class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        result_all = []
        self.combinations(len(num)-1, 2, 0, [], result_all)
        print result_all
        for pair in result_all:
            if pair[0] + pair[1] == target:
                index1 = min(num.index(pair[0]), num.index(pair[1])) + 1
                index2 = max(num.index(pair[0]), num.index(pair[1])) + 1
                return (index1, index2)
        return None
        
    def combinations(self, n, k, level, result, result_all):
        if len(result) == k:
            result_all.append(result)
        else:
            for i in xrange(level, n+1):
                result.append(i)
                self.combinations(n, k, i+1, result, result_all)
                result.pop()
s = Solution()
s.twoSum([3,2,4], 6)