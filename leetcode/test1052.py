class Solution:
    def maxSatisfied(
        self, customers: list[int], grumpy: list[int], minutes: int
    ) -> int:
        ans = 0
        this_turn = 0
        for cus_index in range(len(customers)):
            this_min_cus_num = customers[cus_index]
            this_turn += this_min_cus_num * (1)

            if cus_index < minutes - 1:
                continue
            ans = max(ans, this_turn)
            first_index = cus_index - minutes + 1
            print(this_turn,(customers[first_index] * (1 - grumpy[cus_index])))
            this_turn -= (customers[first_index] * (1 - grumpy[cus_index]))
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.maxSatisfied([3,1,4,1,5,9], [1,1,1,1,1,1], 3))