# Problem: Candy
# Difficulty: Unknown
# Solution:

class Solution:
    def candy(self, ratings: List[int]) -> int:
        count=len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                count+=1
            elif ratings[i] < ratings[i-1]:
                count+=1
        
        return count

        