from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if n == k:
            return sum(cardPoints)

        pre = 0
        suf = 0
        maxi = 0

        for i in range(k):
            pre += cardPoints[i]
        maxi = pre

        for i in range(n-1,n-k-1,-1):
            pre -= cardPoints[i - (n-k)]
            suf += cardPoints[i]
            maxi = max(maxi, pre + suf)

        return maxi
