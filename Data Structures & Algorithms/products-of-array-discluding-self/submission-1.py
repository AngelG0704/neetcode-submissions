class Solution:
    # pref handles all values before index: values <- index (not included)
    # suff handles all values after the index:index(not included) -> values
     def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n #creates result array with size n
        pref = [0] * n #creates pref array with size n
        suff = [0] * n #creates suff array with size n

        pref[0] = 1 # shows that nothing to the left of index 0
        suff[n - 1] = 1 # shows that nothing to the right of last index
        for i in range(1, n): # Goes left to right -->
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1): # goes right to left. <--
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n): 
            res[i] = pref[i] * suff[i] 
        return res