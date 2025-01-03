from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for single_num2 in nums2:
            nums1.append(single_num2)
            nums1.remove(0)

        if len(nums1) >= 2:
            def quick(arr):
                if len(arr) <= 1:
                    return arr
                left, right = [], []
                first = arr[0]
                for single in arr[1:]:
                    if single < first:
                        left.append(single)
                    else:
                        right.append(single)
                return quick(left) + [first] + quick(right)

            i = 0
            for single in quick(nums1):
                nums1[i] = single
                i += 1

if __name__ == '__main__':
    s = Solution()
    nums1 = [2,0]
    nums2 = [1]
    print(s.merge(nums1, 1, nums2, 1))