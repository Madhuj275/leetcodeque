# Problem: Task Scheduler
# Difficulty: Unknown
# Solution:

class Solution:
    def leastInterval(self, tasks, n):  
        if n == 0:
            return len(tasks)
        
        count = Counter(tasks)
        maxi = max(count.values())
        max_tasks = sum( ( 1 for task, val in count.items() if val == maxi ) )
        res = ( maxi-1 )*( n+1 ) + max_tasks
        
        return max(len(tasks), res)