from collections import Counter
from typing import List
class Solution1:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ans = 0
        arr.sort()
        n = len(arr)
        cd = Counter(arr)
        MOD = 10**9 + 7
        for p in range(n):
            l = p + 1
            r = n - 1
            while l < r:

                if arr[p] + arr[l] + arr[r]  > target:
                    r -= 1
                elif arr[p] + arr[l] + arr[r]  < target:
                    l += 1
                elif arr[l] != arr[r]:
                    left = 1
                    right = 1
                    while l + 1 < r and arr[l] == arr[l + 1]:
                        left += 1
                        l += 1
                    while r - 1 > l and arr[r] == arr[r - 1]:
                        right += 1
                        r -= 1
                    ans +=  left * right
                    l +=  1
                    r -=  1
                    ans %= MOD

                else:
                    ans += (r - l + 1) * (r - l) / 2
                    ans %= MOD
                    break

        return int(ans)


if __name__ == '__main__':

    s1 = Solution1()
    print(s1.threeSumMulti([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8))