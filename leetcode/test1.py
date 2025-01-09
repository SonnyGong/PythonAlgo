class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0,len(nums)):
            for j in range(1,len(nums) - 1):
                if nums[i] + nums[j] == target:
                    return [i,j]

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([3,3], 6))