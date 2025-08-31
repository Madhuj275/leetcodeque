class Solution:
    def leastInterval(self, tasks, n):  
        count  = Counter(tasks)
        max_freq = max(count.values())
        c = 0
        for val in count.values():
            if val == max_freq:
                c += 1
        return max(len(tasks),(max_freq-1)*(n+1)+c)