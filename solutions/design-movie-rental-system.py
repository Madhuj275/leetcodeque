# Problem: Design Movie Rental System
# Difficulty: Unknown
# Solution:

from sortedcontainers import SortedSet
class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.movies = {} 
        self.rented = SortedSet() 
        self.shopPrices = {} 
        for entry in entries:
            shop = entry[0]; movie = entry[1]; price = entry[2]
            if movie in self.movies:
                self.movies[movie].add((price, shop))
            else:
                self.movies[movie] = SortedSet()
                self.movies[movie].add((price, shop))
            if shop in self.shopPrices:
                self.shopPrices[shop][movie] = price
            else:
                self.shopPrices[shop] = {}
                self.shopPrices[shop][movie] = price

    def search(self, movie: int) -> List[int]:
        if movie not in self.movies:
            return []
        aval = self.movies[movie]
        candidates = [x[1] for x in aval[:5]]
        return candidates

    def rent(self, shop: int, movie: int) -> None:
        price = self.shopPrices[shop][movie]
        if movie not in self.movies or (price, shop) not in self.movies[movie]:
            return
        self.rented.add((price, shop, movie))
        self.movies[movie].discard((price, shop))

    def drop(self, shop: int, movie: int) -> None:
        price = self.shopPrices[shop][movie]
        if movie not in self.movies:
            return 
        self.movies[movie].add((price, shop))
        self.rented.discard((price, shop, movie))

    def report(self) -> List[List[int]]:
        return [[x[1], x[2]]for x in self.rented[:5]]

