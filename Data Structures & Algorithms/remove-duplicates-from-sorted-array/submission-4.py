class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1 #count of unique, already one since we skipped the first num, which is always unique
        l,r = 1,1 #start at index 1
        while r < len(nums):
            if nums[r] == nums[r-1]:
                r += 1
            elif nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l +=1
                r +=1
                k+=1
        return k