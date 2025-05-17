# Problem: Number of Ways to Arrive at Destination
# Difficulty: Unknown
# Solution:

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        # Dijkstra's algorithm to find the shortest path times
        min_time = [float('inf')] * n
        ways = [0] * n
        min_time[0] = 0
        ways[0] = 1

        heap = [(0, 0)]

        while heap:
            time, node = heappop(heap)

            if time > min_time[node]:
                continue

            for neighbor, travel_time in graph[node]:
                new_time = time + travel_time

                if new_time < min_time[neighbor]:
                    min_time[neighbor] = new_time
                    ways[neighbor] = ways[node]
                    heappush(heap, (new_time, neighbor))

                elif new_time == min_time[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) 

        return ways[n - 1]