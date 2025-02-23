from collections import Counter
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cd = Counter()
        k = 0
        for i in range(0,len(nums)):
            num = nums[i]
            cd[num] += 1
            if cd[num] <= 2:
                nums[k] = num
                k += 1
        return k

if __name__ == '__main__':
    s = Solution()
    nums = [1,1,1,2,2,3]
    print(s.removeDuplicates(nums))
    print(nums)