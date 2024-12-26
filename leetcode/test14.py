class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        first = strs[0]
        others = strs[1:]
        return_str = ""
        this_turn = True
        time_to_end = False
        for index in range(len(first)):
            if time_to_end:
                break
            this_cut_str = first[0:index + 1]
            for single_str in others:
                if this_cut_str != single_str[0:index + 1]:
                    this_turn = False
                if index >= len(single_str) - 1:
                    time_to_end = True

            if this_turn:
                return_str = this_cut_str
            else:
                return return_str
        return return_str

if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["c","acc","ccc"]))