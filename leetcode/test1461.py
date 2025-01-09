class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return_list = []
        temp_c = ""
        for i, c in enumerate(s):
            temp_c += c
            if i < k - 1:
                continue

            return_list.append(temp_c)
            temp_c = temp_c[1:]
        print(return_list)
if __name__ == '__main__':
    s = Solution()
    s.hasAllCodes("00110110", 2)