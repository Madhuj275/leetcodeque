class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def split_by_sign(arr):
            pos, neg = [], []
            for x in arr:
                if x >= 0:
                    pos.append(x)
                else:
                    neg.append(-x)
            return pos, neg[::-1]  
        
        pos1, neg1 = split_by_sign(nums1)
        pos2, neg2 = split_by_sign(nums2)

        total_neg_products = len(pos1) * len(neg2) + len(neg1) * len(pos2)

        if k > total_neg_products:
            k -= total_neg_products
            sign = 1
        else:
            k = total_neg_products - k + 1
            pos2, neg2 = neg2, pos2
            sign = -1

        def count_pairs(A: List[int], B: List[int], cap: int) -> int:
            res = 0
            j = len(B) - 1
            for a in A:
                while j >= 0 and a * B[j] > cap:
                    j -= 1
                res += j + 1
            return res

        low, high = 0, 10**10
        while low < high:
            mid = (low + high) // 2
            count = count_pairs(pos1, pos2, mid) + count_pairs(neg1, neg2, mid)
            if count >= k:
                high = mid
            else:
                low = mid + 1

        return low * sign