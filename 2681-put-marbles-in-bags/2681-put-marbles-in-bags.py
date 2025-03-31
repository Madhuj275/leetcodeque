class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0

        pairs = [weights[i] + weights[i + 1] for i in range(len(weights) - 1)]
        pairs.sort()

        minSplit = sum(pairs[:k - 1])
        maxSplit = sum(pairs[-(k - 1):])

        return maxSplit - minSplit
        