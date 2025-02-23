from collections import Counter
from typing import List


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()

        def single_func(nums1,nums2):
            d1 = Counter(nums1)
            d2 = Counter(nums2)
            nums1 = list(set(nums1))
            nums2 = list(set(nums2))
            nums1.sort()
            nums2.sort()

            n1 = len(nums1)
            n2 = len(nums2)
            ans = 0
            for i in range(n1):
                num1 = nums1[i]
                j = 0
                k = n2 - 1
                while j < k:
                    num2 = nums2[j]
                    num3 = nums2[k]
                    if num1 * num1 == num2 * num3:
                        ans += d1[num1] * d2[num2] * d2[num3]
                        k -= 1
                        j += 1

                    elif num1 * num1 > num2 * num3:
                        j += 1
                    else:
                        k -= 1

                for nn2 in d2.keys():
                    if d2[nn2] > 1:
                        if nn2 == num1:
                            ans += int(d2[nn2]*(d2[nn2]-1)/2*d1[num1])

            return ans

        return single_func(nums1,nums2) + single_func(nums2,nums1)

if __name__ == '__main__':

    solution = Solution()
    print(solution.numTriplets([7,7,8,3],[1,2,9,7]))