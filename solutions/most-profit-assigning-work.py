# Problem: Most Profit Assigning Work
# Difficulty: Unknown
# Solution:

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        max_profit = 0
        j=0 
        pr=0
        temp =[]
        
        for i in range(len(profit)):
            temp.append((difficulty[i], profit[i]))  
        temp.sort()
        worker.sort()

        for w in worker:
            while j < len(temp) and w >= temp[j][0]:
                pr=max(pr,temp[j][1])
                j+=1
            max_profit +=pr
        
        return max_profit
        