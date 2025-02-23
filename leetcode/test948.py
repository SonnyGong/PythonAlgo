from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        n = len(tokens)
        l = 0
        r = n - 1
        ans = 0
        t = 0
        while power > 0 and l <= r:
            if power < tokens[l]:
                break

            power -= tokens[l]
            l += 1
            t += 1
            ans = max(ans, t)
            if l >= n:
                break

            if power < tokens[l] and ans >= 1:
                power += tokens[r]
                r -= 1
                t -= 1
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.bagOfTokensScore([26], 51))

