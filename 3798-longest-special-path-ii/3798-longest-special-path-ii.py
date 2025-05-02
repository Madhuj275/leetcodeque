class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        res = [0, 1]
        graph = defaultdict(list)
        for u,v,cost in edges:
            graph[u].append((v, cost))
            graph[v].append((u, cost))

        curpath = []
        last = defaultdict(lambda: -1)
        
        def dfs(node, curr_cost, prev,seen):
            lastcolor = last.get(nums[node], -1) 
            last[nums[node]] = len(curpath) 
            curpath.append(curr_cost)
            start = seen[0] 

            if curr_cost - curpath[start] > res[0]:
                res[0] = curr_cost - curpath[start]
                res[1] = len(curpath) - start
            elif curr_cost - curpath[start] == res[0]:
                res[1] = min(res[1], len(curpath) - start)

            for next_node, next_cost in graph[node]:
                if next_node == prev:
                    continue
                
                nextstart = seen 
                if last[nums[next_node]] != -1 and start <= last[nums[next_node]]:
                    nextstart = seen + [last[nums[next_node]] + 1]
                    
             
                dfs(next_node, curr_cost + next_cost, node, sorted(nextstart)[-2:])
            
            last[nums[node]] = lastcolor
            curpath.pop()
        
        dfs(0, 0, -1,[0,0])
        return res