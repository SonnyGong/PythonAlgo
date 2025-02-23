from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        while l < r:
            while nums[r] % 2 != 0 and nums[r] != 0:
                r -= 1
                if r < 0 or l >= r:
                    return nums

            if nums[l] % 2 == 0:
                l += 1

            else:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums

if __name__ == '__main__':
    s = Solution()
    print(s.sortArrayByParity([1,3,0]))
