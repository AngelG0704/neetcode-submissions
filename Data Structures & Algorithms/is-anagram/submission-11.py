class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        validI = {}
        validJ = {}

        for i in s:
            validI[i] = validI.get(i,0) + 1
        for j in t:
            validJ[j] = validJ.get(j,0)+1
        return validI == validJ