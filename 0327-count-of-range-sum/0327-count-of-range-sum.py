class SegmentTree:
    class Node:
        def __init__(self, start, end):
            self.start = start
            self.end = end
            self.left = None
            self.right = None
            self.count = 0
    
    def __init__(self, start, end):
        def _build(start, end):
            if start > end:
                return None
            if start == end:
                return SegmentTree.Node(start, end)
            
            mid = (start + end) // 2
            node = SegmentTree.Node(start, end)
            node.left = _build(start, mid)
            node.right = _build(mid + 1, end)
            return node
        self.root = _build(start, end)
    
    def update(self, ind):
        def _update(node):
            if not node or node.start > ind or node.end < ind:
                return
            if node.start == node.end == ind:
                node.count += 1
                return
                     
            _update(node.left)
            _update(node.right)
            node.count = node.left.count + node.right.count

        _update(self.root)
    
    def query(self, query_start, query_end):
        def _query(node):
            if not node or node.start > query_end or node.end < query_start:
                return 0
            if node.start >= query_start and node.end <= query_end:
                return node.count
            
            return _query(node.left) + _query(node.right)
        return _query(self.root)
    
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        presums = [0]
        for num in nums:
            presums.append(presums[-1] + num)
        
        # compress all possible presums, and potential query bounds to index
        possible_all_sums = []
        for presum in presums:
            possible_all_sums.append(presum)
            possible_all_sums.append(presum - upper)
            possible_all_sums.append(presum - lower)
        sums_to_ind = {s:ind for ind, s in enumerate(sorted(set(possible_all_sums)))}

        segmentTree = SegmentTree(0, len(sums_to_ind) - 1)

        result = 0
        for presum in presums:
            low = sums_to_ind[presum - upper]
            high = sums_to_ind[presum - lower]
            result += segmentTree.query(low, high)
            segmentTree.update(sums_to_ind[presum])
        return result