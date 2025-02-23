from collections import Counter


class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count('1') < k:
            return ''
        left = 0
        ans = len(s)
        cd = Counter()
        have = 0
        return_s = s
        for right, c in enumerate(s):
            cd[c] += 1
            while cd['1'] > k or s[left] == '0':
                cd[s[left]] -= 1
                left += 1

            if cd['1'] == k:

                if len(s[left: right + 1]) < ans or len(s[left: right + 1]) == ans and return_s > s[left: right + 1]:
                    return_s = s[left: right + 1]
                    ans = len(return_s)
        return return_s if cd['1'] == k else ''

if __name__ == '__main__':
    s = Solution()
    print(s.shortestBeautifulSubstring("1111111011111", 12))