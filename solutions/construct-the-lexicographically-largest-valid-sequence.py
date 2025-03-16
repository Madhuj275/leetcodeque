# Problem: Construct the Lexicographically Largest Valid Sequence
# Difficulty: Unknown
# Solution:

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        sequence = [0] * (2 * n - 1)
        seen = set()
        def dfs(i):
            if i == len(sequence):
                return True
            if sequence[i]:
                return dfs(i + 1)
            for j in range(n, 0, - 1):
                if j in seen:
                    continue
                seen.add(j)
                sequence[i] = j
                if j == 1:
                    if dfs(i + 1):
                        return True
                elif i + j < len(sequence) and sequence[i + j] == 0:
                    sequence[i + j] = j
                    if dfs(i + 1):
                        return True
                    sequence[i + j] = 0
                sequence[i] = 0
                seen.remove(j)
            return False
        dfs(0)
        return sequence
