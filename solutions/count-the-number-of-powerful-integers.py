# Problem: Count the Number of Powerful Integers
# Difficulty: Unknown
# Solution:

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        count = 0

        for num in range(start, finish + 1):
            num_str = str(num)
            valid = True

            for ch in num_str:
                if int(ch) > limit:
                    valid = False
                    break

            if not num_str.endswith(s):
                valid = False

            if valid:
                count += 1

        return count
