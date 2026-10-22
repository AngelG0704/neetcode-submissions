class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0,len(numbers)-1
        while l < r:
            if numbers[r] + numbers[l] > target: #Value too big
                r -=1
            if numbers[r] + numbers[l] < target: #Value too small
                l +=1
            if numbers[r] + numbers[l] == target: #Value is equal
                return [l+1, r+1]