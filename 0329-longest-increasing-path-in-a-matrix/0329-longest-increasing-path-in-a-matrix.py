class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])

        # answer_map[i][j] will hold maximum path length starting from (i, j) point.
        answer_map = [[None for _ in range(n)] for _ in range(m)]

        def dfs(i, j):
            # At first, the depth (path length) is one, just the point we are on (i, j)
            depth = 1

            # If we have already found the answer for this point, just return it
            if answer_map[i][j]:
                return answer_map[i][j]

            points_of_interest = [
                (i + 1, j),
                (i - 1, j),
                (i, j + 1),
                (i, j - 1),
            ]
            for x, y in points_of_interest:
                # Check if we are in borders
                # And then check if the value of the next point is lower
                if (x >= 0 and x < m and y >= 0 and y < n) and (
                    matrix[x][y] > matrix[i][j]
                ):
                    depth = max(depth, dfs(x, y) + 1)

            # Update the answer map with the new maximum path length (depth)
            answer_map[i][j] = depth
            return depth

        # Run this recursive function from every point of the matrix
        for i, j in [(i, j) for i in range(m) for j in range(n)]:
            dfs(i, j)

        # Return the maximum path from the answer_map
        return max(max(row) for row in answer_map)