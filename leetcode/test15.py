class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        print(nums)
        length = len(nums)

        return_ans = []
        for first_index in range(length):
            right_pointer = length - 1
            first_num = nums[first_index]
            print("第一个数",first_num)
            if first_index > 0 and first_num == nums[first_index - 1]:
                continue
            to_search_sum = -first_num
            for left_pointer in range(first_index + 1, length):

                if left_pointer > first_index + 1 and nums[left_pointer] == nums[left_pointer - 1]:
                    continue




                while nums[left_pointer] + nums[right_pointer] > to_search_sum and left_pointer < right_pointer:
                    right_pointer -= 1

                if left_pointer == right_pointer:
                    break
                if nums[left_pointer] + nums[right_pointer] == to_search_sum:
                    return_ans.append([first_num, nums[left_pointer], nums[right_pointer]])
        return return_ans


class Solution2:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        ans = list()

        # 枚举 a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
            # 枚举 b
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans

if __name__ == '__main__':

    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))