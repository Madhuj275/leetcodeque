class Solution(object):
    def goodTriplets(self, nums1, nums2):
        n = len(nums1)
        index_map = {val: i for i, val in enumerate(nums1)}
        mapped_nums2 = [index_map[val] for val in nums2]
        smaller = [0] * n
        greater = [0] * n

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            merged = []
            i = j = 0
            len_left = len(left)
            len_right = len(right)
            while i < len_left and j < len_right:
                if right[j] < left[i]:
                    val = right[j]
                    smaller[val] += bisect.bisect_right(left, val)
                    merged.append(val)
                    j += 1
                else:
                    val = left[i]
                    greater[val] += len_right - bisect.bisect_right(right, val)
                    merged.append(val)
                    i += 1
            while i < len_left:
                val = left[i]
                greater[val] += len_right - bisect.bisect_right(right, val)
                merged.append(val)
                i += 1
            while j < len_right:
                val = right[j]
                smaller[val] += bisect.bisect_right(left, val)
                merged.append(val)
                j += 1
            return merged

        merge_sort(mapped_nums2)
        return sum(smaller[i] * greater[i] for i in range(n))