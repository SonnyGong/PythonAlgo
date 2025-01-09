class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        length_p = len(p)
        temp_num = 0
        return_list = []
        temp_list = [i for i in p]
        print(temp_list)
        for i,c in enumerate(s):
            if c in temp_list:
                temp_list.remove(c)
                temp_num += 1
                if temp_num == length_p:
                    return_list.append(i - length_p + 1)
            else:
                temp_num = 0
                temp_list = [i for i in p]
        return return_list
if __name__ == '__main__':
    sol = Solution()
    print(sol.findAnagrams("cbaebabacd", "abc"))