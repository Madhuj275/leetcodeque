@cache
def isPrimeScore(num):
    score = 0
    if num % 2 == 0:
        score += 1
        while num % 2 == 0:
            num //= 2
    for p in range(3, int(sqrt(num)) + 1, 2):
        if num % p == 0:
            score += 1
            while num % p == 0:
                num //= p
    if num > 1:
        score += 1
    return score 

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        scores = [isPrimeScore(num) for num in nums] + [MOD]
        lefts = [0] * len(nums)
        stack = [-1]
        for i in range(len(nums)):
            while scores[i] > scores[stack[-1]]:
                stack.pop()
            lefts[i] = stack[-1]
            stack.append(i)
        rights = [0] * len(nums)
        stack = [len(nums)]

        for i in reversed(range(len(nums))):
            while scores[i] >= scores[stack[-1]]:
                stack.pop()
            rights[i] = stack[-1]
            stack.append(i)

        max_score = 1
        for num, i in sorted(((num, i) for i, num in enumerate(nums)), reverse = True):
            count = (i - lefts[i]) * (rights[i] - i)
            max_score *= pow(num, min(k, count), MOD )
            max_score %= MOD 
            if count >= k:
                break
            k -= count
        return max_score
