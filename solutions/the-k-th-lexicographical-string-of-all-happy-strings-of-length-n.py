# Problem: The k-th Lexicographical String of All Happy Strings of Length n
# Difficulty: Unknown
# Solution:

from collections import deque

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        size_n = []
        q = deque()

        q.append("a")
        q.append("b")
        q.append("c")

        while q:
            curr = q.popleft()
            if len(curr) == n:
                size_n.append(curr)
                continue

            last_char = curr[-1]
            if last_char == 'a':
                q.append(curr + 'b')
                q.append(curr + 'c')
            elif last_char == 'b':
                q.append(curr + 'a')
                q.append(curr + 'c')
            else:
                q.append(curr + 'a')
                q.append(curr + 'b')

        if len(size_n) < k:
            return ""
        return size_n[k - 1]