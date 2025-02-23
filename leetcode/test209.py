class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        s = 0
        ans = len(nums)
        for right,c in enumerate(nums):
            print("轮询到",right,"数字为",c)
            while s >= target:

                ans = min(ans,right - left + 1)

                s -= nums[left]
                left += 1
            s += c
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(4, [1,4,4]))