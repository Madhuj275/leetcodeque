# Problem: Shifting Letters II
# Difficulty: Unknown
# Solution:

class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        shifts_applied = [0] * n  
        for start, end, direction in shifts:
            if direction ==1:
                value=1
            else:
                value=-1
            for i in range(start, end + 1):  
                shifts_applied[i] += value

        shifted_s = list(s)
        for i in range(n):
            shift = (ord(shifted_s[i]) - ord('a') + shifts_applied[i]) % 26
            if shift < 0:
                shift += 26  
            shifted_s[i] = chr(ord('a') + shift)

        return ''.join(shifted_s)


        