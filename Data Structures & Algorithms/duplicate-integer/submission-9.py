class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        non_dupe = {}

        for n in nums:
            if n in non_dupe:
                return True
            non_dupe[n] = n
        return False