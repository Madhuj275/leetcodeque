# Problem: Delete Duplicate Folders in System
# Difficulty: Unknown
# Solution:

from collections import defaultdict
from typing import List

class Directory:
    def __init__(self):
        self.subdirectories = defaultdict(Directory)
        self.marked_for_deletion = False

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        def get_signature(directory):
            signature = "(" + "".join(subdir + get_signature(directory.subdirectories[subdir]) for subdir in directory.subdirectories) + ")"
            if signature != "()":
                signature_map[signature].append(directory)
            return signature
        
        def collect_unique_paths(directory, current_path):
            for subdir in directory.subdirectories:
                if not directory.subdirectories[subdir].marked_for_deletion:
                    collect_unique_paths(directory.subdirectories[subdir], current_path + [subdir])
            if current_path:
                result_paths.append(current_path[:])
        
        signature_map, root_directory, result_paths = defaultdict(list), Directory(), []
        
        for path in sorted(paths):
            current_directory = root_directory
            for part in path:
                current_directory = current_directory.subdirectories[part]
        
        get_signature(root_directory)
        
        for directories in signature_map.values():
            if len(directories) > 1:
                for directory in directories:
                    directory.marked_for_deletion = True
        
        collect_unique_paths(root_directory, [])
        return result_paths