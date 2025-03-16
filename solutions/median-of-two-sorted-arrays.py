# Problem: Median of Two Sorted Arrays
# Difficulty: Unknown
# Solution:

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findKth(A, B, k, aStart, aEnd, bStart, bEnd):
            aLen = aEnd - aStart + 1
            bLen = bEnd - bStart + 1
            if aLen == 0:
                return B[bStart + k]
            if bLen == 0:
                return A[aStart + k]
            if k == 0:
                return min(A[aStart], B[bStart])
            aMid = aLen * k // (aLen + bLen)
            bMid = k - aMid - 1
            aMid += aStart
            bMid += bStart
            if A[aMid] > B[bMid]:
                k -= (bMid - bStart + 1)
                aEnd = aMid
                bStart = bMid + 1
            else:
                k -= (aMid - aStart + 1)
                bEnd = bMid
                aStart = aMid + 1
            return findKth(A, B, k, aStart, aEnd, bStart, bEnd)

        m, n = len(nums1), len(nums2)
        if (m + n) % 2 != 0:
            return findKth(nums1, nums2, (m + n) // 2, 0, m - 1, 0, n - 1)
        else:
            return (findKth(nums1, nums2, (m + n) // 2, 0, m - 1, 0, n - 1) + 
                    findKth(nums1, nums2, (m + n) // 2 - 1, 0, m - 1, 0, n - 1)) * 0.5

        