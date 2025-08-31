class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:   
            return image

        Q = deque()
        Q.append((sr, sc))
        a = image[sr][sc]
        M, N = len(image), len(image[0])
        image[sr][sc] = color   

        while Q:
            i, j = Q.popleft()
            for r, c in [(i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)]:
                if 0 <= r < M and 0 <= c < N and image[r][c] == a:
                    image[r][c] = color
                    Q.append((r, c))

        return image
