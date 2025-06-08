class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        stack = []
        result = []

        for i in range(9, 0, -1):
            if i <= n:
                stack.append(i)

        while stack:
            num = stack.pop()
            result.append(num)

            for i in range(9, -1, -1):
                next_num = num * 10 + i
                if next_num <= n:
                    stack.append(next_num)

        return result
