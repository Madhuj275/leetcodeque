class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source==destination:
            return True
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        seen=set()
        seen.add(source)
        stack=[]
        stack.append(source)

        while stack:
            i=stack.pop()
            if i==destination:
                return True
            for j in graph[i]:
                if j not in seen:
                    seen.add(j)
                    stack.append(j)
            
        
        return False
                
        