# Problem: Set Mismatch
# Difficulty: Unknown
# Solution:

class Solution:
    def findErrorNums(self, arr: list[int]) -> list[int]:
        n = len(arr)
        seen = set()
        duplicate = 0
        missing = 0

        for num in arr:
            if num in seen:
                duplicate = num
            else:
                seen.add(num)

        for i in range(1, n + 1):
            if i not in seen:
                missing = i
                break

        return [duplicate, missing]


        