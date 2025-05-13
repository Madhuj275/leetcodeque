# Problem: Minimum Cost to Split an Array
# Difficulty: Unknown
# Solution:

class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        result = [0]
        nums = [-1] + nums

        def compute_cost(position):
            frequency = defaultdict(int)
            accumulated_cost = 0
            minimum_cost = float('inf')
            while position > 0:
                if frequency[nums[position]] > 0:
                    accumulated_cost += 1
                    if frequency[nums[position]] == 1:
                        accumulated_cost += 1
                frequency[nums[position]] += 1
                minimum_cost = min(result[position - 1] + accumulated_cost, minimum_cost)
                position -= 1
            return minimum_cost + k

        for pos in range(1, len(nums)):
            result.append(compute_cost(pos))

        return result[-1]