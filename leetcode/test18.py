from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        R = n - 1
        L = 0
        return_list = []
        for L in range(n - 3):
            if L and nums[L] == nums[L - 1]:
                continue
            for R in range(n-1, 2, -1):
                if R < n - 1 and nums[R] == nums[R + 1]:
                    continue
                l = L + 1
                r = R - 1
                while l < r:
                    x = nums[L] + nums[l] + nums[r] + nums[R]
                    print(x)
                    if r > l > L + 1 and nums[l] == nums[l - 1]:
                        l += 1
                        continue
                    if R - 1 > r > l and nums[r] == nums[r + 1]:
                        r -= 1
                        continue
                    if x == target:
                        return_list.append([nums[L], nums[l], nums[r], nums[R]])
                        l += 1
                        r -= 1
                    elif x > target:
                        r -= 1
                    else:
                        l += 1
        return return_list

if __name__ == '__main__':
    sol = Solution()
    print(sol.fourSum(
[2,2,2,2,2], 8))

