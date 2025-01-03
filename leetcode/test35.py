class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left_pointer = 0
        right_pointer = len(nums) - 1
        middle_pointer = 0
        while left_pointer <= right_pointer:
            middle_pointer = (left_pointer + right_pointer) //2
            if nums[middle_pointer] > target:
                right_pointer = middle_pointer - 1
            elif nums[middle_pointer] < target:
                left_pointer = middle_pointer + 1
            else:
                return middle_pointer
        return left_pointer


if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1,3,5,6], 3))