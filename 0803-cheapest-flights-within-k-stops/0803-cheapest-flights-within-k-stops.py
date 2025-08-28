class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph=defaultdict(list)
        for u,v,w in flights:
            graph[u].append((v,w))
        
        visited = [float('inf')] * n
        visited[src] = 0
        q=deque()
        q.append((src,0))
        k+=1
        while k > 0 and q:
            le=len(q)
            while le >0:
                i,j=q.popleft()
                for nei,price in graph[i]:
                    newprice=j+price
                    if newprice < visited[nei]:
                        visited[nei] = newprice
                        q.append((nei,newprice))
                le-=1
            k-=1
        
        return visited[dst] if visited[dst] != float('inf') else -1





        

        