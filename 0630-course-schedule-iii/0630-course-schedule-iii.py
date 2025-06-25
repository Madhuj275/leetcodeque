class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = sorted(courses,key=lambda x : x[1])
        pq = []
        heapq.heapify(pq)
        count = 0
        for u,v in courses:
            heapq.heappush(pq,-1*u)
            count += u
            if count > v:
                a = heapq.heappop(pq)
                count += a
        res = 0
        while pq:
            res += 1
            heapq.heappop(pq)
        return res
