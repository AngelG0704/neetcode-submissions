class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            #creates a list of 26 indices to match the 26 char in a-z
            count = [0] * 26
            for c in s:
                # This sets the index to a single digit since for ex. c is 82 and a is 80
                # when we subtract the two we get: 2, which is a valid index in our count list
                # we do += 1 since we are counting the amount of times we see this char by 1 
                count[ord(c)-ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())