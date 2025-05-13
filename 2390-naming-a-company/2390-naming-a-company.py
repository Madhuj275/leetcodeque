class Solution(object):
      def distinctNames(self, ideas):
        hn = {}
        for idea in ideas:
            hn[idea] = True
        dict = [[0 for j in range(26)] for i in range(26)]
        for idea in ideas:
            word = idea[1:]
            index = ord(idea[0]) - ord('a')
            for j in range(26):
                temp = chr(ord('a') + j) + word
                if temp not in hn:
                    dict[index][j] += 1
                
        count = 0
        for i in range(26):
            for j in range(26):
                if dict[i][j] == 0:
                    continue
                count += (dict[i][j] * dict[j][i])
        return count
        