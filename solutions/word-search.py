# Problem: Word Search
# Difficulty: Unknown
# Solution:

class Solution:
    def exist(self, maze, word):
        def search(row, col, idx):
            if idx == len(word):
                return True
            if row < 0 or col < 0 or row >= len(maze) or col >= len(maze[0]) or maze[row][col] != word[idx]:
                return False
            maze[row][col] = '*'
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                if search(row + dr, col + dc, idx + 1):
                    return True
            maze[row][col] = word[idx]
            return False

        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if maze[i][j] == word[0] and search(i, j, 0):
                    return True
        return False


        