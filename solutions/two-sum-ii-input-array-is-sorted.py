# Problem: Two Sum II - Input Array Is Sorted
# Difficulty: Unknown
# Solution:

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        res=[]
        for i in range(n-1):
            for j in range(i+1,n):
                if (numbers[i] + numbers[j] == target):
                    res.append(i+1)
                    res.append(j+1)
        return res

