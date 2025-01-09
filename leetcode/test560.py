class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        ans = 0
        temp_sum = []
        pointer = 0
        while pointer < len(nums):
            if len(temp_sum) > 0:
                if sum(temp_sum) < k and sum(temp_sum) > 0:
                    pointer += 1
                elif sum(temp_sum) == k:
                    ans += 1
                    pointer += 1
                    temp_sum.pop(0)

                elif sum(temp_sum) > k:
                    if pointer == len(nums) - 1 and len(temp_sum) < 2:
                        return ans
                    else:
                        temp_sum.pop(0)
                        continue
            if pointer < len(nums):
                temp_sum.append(nums[pointer])

        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.subarraySum([-1,-1,1], 0))