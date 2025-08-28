from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if n == k:
            return sum(cardPoints)

        pre = 0
        suf = 0
        maxi = 0

        # prefix: take from start
        for i in range(k):
            pre += cardPoints[i]
        maxi = pre

        # suffix: slide backwards, reduce prefix, add suffix
        for i in range(1, k+1):
            pre -= cardPoints[k-i]
            suf += cardPoints[n-i]
            maxi = max(maxi, pre + suf)

        return maxi
