class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        g_max = 0
        l_max = 0
        for n in nums:
            if n == 0:
                l_max = 0
            else:
                l_max = l_max + 1
            if l_max > g_max:
                g_max = l_max
        return g_max