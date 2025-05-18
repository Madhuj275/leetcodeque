# Problem: Word Search II
# Difficulty: Unknown
# Solution:

class Solution(object):
    def findWords(self, board, words):
        out = []
        class node:
            def __init__(self):
                self.word = -1
                self.d = {}
        root = node()
        
        def insert(s, i):
            t = root
            for c in s:
                if c not in t.d:
                    t.d[c] = node()
                t = t.d[c]
            t.word = i
        
        for i in range(len(words)):
            insert(words[i], i)
        
        directions= [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def find(i, j, r):
            if r.word!=-1:
                out.append(words[r.word])
                r.word=-1
            for d in directions:
                x =  d[0]+i
                y =  d[1]+j
                if 0<= x< len(board) and 0<=y < len(board[0]) and board[x][y] in r.d:
                    t = board[x][y]
                    board[x][y] = ""
                    find(x, y, r.d[t])
                    board[x][y] = t

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root.d:
                    t = board[i][j]
                    board[i][j] = ""
                    find(i, j, root.d[t])
                    board[i][j] = t
        return out