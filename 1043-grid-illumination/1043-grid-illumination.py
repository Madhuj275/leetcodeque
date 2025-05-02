class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        def check(i, j, dRow, dCol, dDiagS, dDiagP):
            if (i in dRow and dRow[i] > 0) or (j in dCol and dCol[j] > 0) or (
                    i + j in dDiagS and dDiagS[i + j] > 0) or (
                    i - j in dDiagP and dDiagP[i - j] > 0):
                return True
            return False
        
        def decrement(i, j, dRow, dCol, dDiagS, dDiagP):
            dRow[i] -= 1
            dCol[j] -= 1
            dDiagS[i + j] -= 1
            dDiagP[i - j] -= 1
        
        my_set = set()
        dRow, dCol, dDiagS, dDiagP = {}, {}, {}, {} 
        for i in range(len(lamps)):
            if (lamps[i][0], lamps[i][1]) not in my_set:
                if lamps[i][0] not in dRow:
                    dRow[lamps[i][0]] = 1
                else:
                    dRow[lamps[i][0]] += 1
                if lamps[i][1] not in dCol:
                    dCol[lamps[i][1]] = 1
                else:
                    dCol[lamps[i][1]] += 1
                if sum(lamps[i]) not in dDiagS:
                    dDiagS[sum(lamps[i])] = 1
                else:
                    dDiagS[sum(lamps[i])] += 1
                if lamps[i][0] - lamps[i][1] not in dDiagP:
                    dDiagP[lamps[i][0] - lamps[i][1]] = 1
                else:
                    dDiagP[lamps[i][0] - lamps[i][1]] += 1
                my_set.add((lamps[i][0], lamps[i][1]))
        ans = []
        directions = [(-1, -1), (-1, 0), (0, -1), (0, 0), (0, 1), (1, 0), (1, 1), (1, -1), (-1, 1)]
        for i in range(len(queries)):
            if check(queries[i][0], queries[i][1], dRow, dCol, dDiagS, dDiagP):
                ans.append(1)
                for x in directions:
                    if (queries[i][0]+x[0], queries[i][1]+x[1]) in my_set:
                        decrement(queries[i][0]+x[0], queries[i][1]+x[1], dRow, dCol, dDiagS, dDiagP)
                        my_set.remove((queries[i][0]+x[0], queries[i][1]+x[1]))
            else:
                ans.append(0)
        return ans