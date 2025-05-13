class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        start, end = 0, 0
        last_idx = {c: idx for idx, c in enumerate(s)}

        for i, c in enumerate(s):
            end = max(end, last_idx[c]) 

            if i == end:
                res.append(end - start + 1)
                start = i + 1
                
        return res