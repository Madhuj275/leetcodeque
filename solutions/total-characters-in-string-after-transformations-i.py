# Problem: Total Characters in String After Transformations I
# Difficulty: Unknown
# Solution:

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        while t > 0:
            result=''
            for char in s:
                if char == 'z':
                    result += 'ab'
                elif 'a' <= char <= 'y':
                    result += chr(ord(char) + 1)
                else:
                    result += char
            t-=1
            s=result

        return len(result)
        