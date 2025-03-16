# Problem: Find Unique Binary String
# Difficulty: Unknown
# Solution:

class Solution:
    def __init__(self):
        self.res = ""

    def buildNumber(self, numbers, curr, n):
        if len(curr) == n:
            if curr not in numbers:
                self.res = curr
                return True
            return False

        if self.buildNumber(numbers, curr + '0', n):
            return True

        if self.buildNumber(numbers, curr + '1', n):
            return True

        return False

    def findDifferentBinaryString(self, nums):
        n = len(nums)
        numbers = set(nums)
        self.buildNumber(numbers, "", n)
        return self.res