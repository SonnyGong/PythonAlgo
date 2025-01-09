class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        def quicksort(arr):
            if len(arr) <= 1:
                return arr
            first = arr[0]
            left,right = [],[]
            for temp in arr[1:]:
                if temp < first:
                    left.append(temp)
                else:
                    right.append(temp)
            return quicksort(left) + [first] + quicksort(right)
        nums = quicksort(nums)
        return_turns_list = []
        return_nums = 0
        for single_index in range(1,len(nums)):
            if nums[single_index] - nums[single_index - 1] != 1:
                return_turns_list.append(single_index - return_nums)
                return_nums = single_index
        return_turns_list.append(len(nums) - return_nums)
        return max(return_turns_list)
if __name__ == '__main__':
    sol = Solution()
    print(sol.longestConsecutive([1,2,0,1]))