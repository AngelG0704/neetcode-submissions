class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        width, height = 0,0
        globalArea, localArea = 0,0        

        if len(heights) < 2:
            return 0

        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            localArea = width * height
            if localArea > globalArea:
                globalArea = localArea
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return globalArea
