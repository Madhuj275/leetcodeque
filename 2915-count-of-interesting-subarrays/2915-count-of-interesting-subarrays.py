class Solution:
    def countInterestingSubarrays(self, nums, modulo, k):
        count = 0
        count_map = defaultdict(int)
        count_map[0] = 1
        result = 0

        for num in nums:
            if num % modulo == k:
                count += 1
            key = (count - k) % modulo
            result += count_map[key]
            count_map[count % modulo] += 1

        return result