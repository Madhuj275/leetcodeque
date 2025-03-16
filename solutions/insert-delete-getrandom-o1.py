# Problem: Insert Delete GetRandom O(1)
# Difficulty: Unknown
# Solution:

import random

class RandomizedSet:
    def __init__(self):
        self.hash_map = {}  # Maps value to its index in the array
        self.array = []     # Stores the actual values

    def insert(self, val: int) -> bool:
        if val in self.hash_map:
            return False  # Assuming duplicates are not allowed
        self.hash_map[val] = len(self.array)
        self.array.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash_map:
            return False
        index = self.hash_map[val]
        del self.hash_map[val]
        if index != len(self.array) - 1:
            last_val = self.array[-1]
            self.array[index] = last_val
            self.hash_map[last_val] = index
        self.array.pop()
        return True

    def getRandom(self) -> int:
        if not self.array:
            raise ValueError("Set is empty")
        return random.choice(self.array)

# Example usage:
randomized_set = RandomizedSet()
print(randomized_set.insert(1))  # Should print: True
print(randomized_set.insert(2))  # Should print: True
print(randomized_set.insert(3))  # Should print: True
print(randomized_set.getRandom())  # Randomly returns 1, 2, or 3
print(randomized_set.remove(2))    # Should print: True
print(randomized_set.getRandom())  # Randomly returns 1 or 3
