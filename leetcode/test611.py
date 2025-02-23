from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        n = len(nums)
        for R in range(n-1,1,-1):
            l = 0
            r = l + 1
            while r < R:
                if r + l > R:
                    ans += R - r + 1
                else:
                    l += 1
                    r += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.triangleNumber([2,2,3,4]))