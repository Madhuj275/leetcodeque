# Problem: H-Index
# Difficulty: Unknown
# Solution:

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h=0
        citations.sort(reverse=True)
        if len(citations) == 1:
            return nums[0]
        for i in range(len(citations)):
            if citations[i] >= i+1:
                h+=1
            else:
                return h

        