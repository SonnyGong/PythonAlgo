class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        this_turn_average = 0
        return_list = [0] * len(nums)
        for i, single in enumerate(nums):
            print("加上：",single)
            this_turn_average += single

            if i < 2 * k + 1 - 1:
                return_list[i] = -1
                continue



            return_list[i - k] = this_turn_average // (2 * k + 1)
            print("减去：",nums[i - k - 1 + 1])
            this_turn_average -= nums[i - 2 * k - 1 + 1]

            if len(nums) - 1 - i < k:
                return_list[i] = -1



        return return_list

if __name__ == '__main__':
    s = Solution()
    print(s.getAverages([7,4,3,9,1,8,5,2,6], 3))