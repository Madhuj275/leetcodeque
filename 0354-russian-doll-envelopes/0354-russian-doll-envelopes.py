import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Sort envelopes: increasing width, and if widths are equal, decreasing height
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # We now extract the heights and find the length of the longest increasing subsequence (LIS)
        heights = [h for _, h in envelopes]
        lis = []
        
        for h in heights:
            # Find the insertion point
            i = bisect.bisect_left(lis, h)
            if i == len(lis):
                lis.append(h)
            else:
                lis[i] = h
        return len(lis)