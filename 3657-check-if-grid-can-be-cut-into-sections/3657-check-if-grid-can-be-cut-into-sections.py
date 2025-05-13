class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        
        line = []
        for rect in rectangles:
            line.append((rect[0], 1))
            line.append((rect[2], 0))

        # sort by x
        line.sort()
        res = 0
        curr_amount = 1
        for i in range(1, len(line)-1):
            if line[i][1] == 1: # start
                curr_amount += 1
            else:
                curr_amount -= 1

            if curr_amount == 0:
                res += 1
        
        if res >= 2:
            return True
        
        # sort by y
        line = []
        for rect in rectangles:
            line.append((rect[1], 1))
            line.append((rect[3], 0))

        line.sort()
        res = 0
        curr_amount = 1
        for i in range(1, len(line)-1):
            if line[i][1] == 1: # start
                curr_amount += 1
            else:
                curr_amount -= 1

            if curr_amount == 0:
                res += 1
        
        return res >= 2