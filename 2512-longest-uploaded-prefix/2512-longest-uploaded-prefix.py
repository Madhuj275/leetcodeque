class LUPrefix:

    def __init__(self, n: int):
        self.videos = [False] * (n + 1)
        self.prefix = 0

    def upload(self, video: int) -> None:
        self.videos[video-1] = True
        while self.videos[self.prefix]:
            self.prefix += 1

    def longest(self) -> int:
        return self.prefix