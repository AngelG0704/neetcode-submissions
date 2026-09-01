class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe = {}


        for i in nums:
            value = i
            if value in dupe:
                return True
            dupe[value] = True
        return False
