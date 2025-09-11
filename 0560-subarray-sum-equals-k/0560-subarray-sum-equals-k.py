class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        freq = defaultdict(int)
        freq[0] = 1   

        for num in nums:
            prefix_sum += num
            if (prefix_sum - k) in freq:
                count += freq[prefix_sum - k]
            freq[prefix_sum] += 1

        return count