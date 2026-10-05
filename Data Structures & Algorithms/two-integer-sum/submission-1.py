class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        pair = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in pair:
                return [pair[complement], i]
            pair[nums[i]] = i