# Problem: Total Characters in String After Transformations I
# Difficulty: Unknown
# Solution:

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        while t > 0:
            chars = []
            for char in s:
                if char == 'z':
                    chars.extend(['a', 'b'])
                elif 'a' <= char <= 'y':
                    chars.append(chr(ord(char) + 1))
                else:
                    chars.append(char)
            s = ''.join(chars)
            t -= 1
        return len(s)
