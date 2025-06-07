class Solution:
    def clearStars(self, s: str) -> str:
        h = []
        stacks = [[] for _ in range(26)]
        for i, c in enumerate(s):
            if c == "*":
                while h and not stacks[h[0]]:
                    heapq.heappop(h)
                if h:
                    stacks[h[0]].pop()
            else:
                x = ord(c) - 97
                if not stacks[x]:
                    heapq.heappush(h, x)
                stacks[x].append(i)
        return "".join(s[i] for i in sorted(itertools.chain.from_iterable(stacks)))