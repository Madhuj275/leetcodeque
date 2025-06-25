from sortedcontainers import SortedList # To help us add/removing elements from/to sorted list in log(N) time
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        add_building = 0
        remove_building = 1

        events = defaultdict(list)
        unique_x = set()
        for l, r, h in buildings:
            unique_x.add(l)
            unique_x.add(r)
            events[l].append((add_building, h))
            events[r].append((remove_building, h))

        ret = []
        heights= SortedList([0]) 
        for x in sorted(list(unique_x)): 
            for action, h in sorted(events[x]):
                if action == add_building:
                    heights.add(h)
                else:
                    heights.remove(h)
            if len(ret)==0 or ret[-1][1]!=heights[-1]:
                ret.append((x, heights[-1]))
        return ret