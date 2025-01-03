class Solution:
    def climbStairs(self, n: int) -> int:
        dict1 = {}
        def small_func(n,dict1):
            if n == 1 or n == 0:
                return 1
            else:
                if n in dict1:
                    return dict1[n]
                else:
                    dict1[n - 1] = small_func(n -1,dict1)
                    dict1[n - 2] = small_func(n -2,dict1)
                    return dict1[n - 1] + dict1[n - 2]
        return small_func(n,dict1)

if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(2))