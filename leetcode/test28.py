class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        short_pointer_index = 0
        long_pointer_index = 0
        FIND = True
        record_index = -1
        while long_pointer_index < len(haystack) and short_pointer_index < len(needle):
            print(haystack[long_pointer_index], needle[short_pointer_index])
            if haystack[long_pointer_index] == needle[short_pointer_index]:
                if record_index == -1:
                    record_index = long_pointer_index
                short_pointer_index += 1
                FIND = True
            else:
                FIND = False
                record_index = -1
                short_pointer_index = 0

            long_pointer_index += 1
        if FIND:
            return record_index
        else:
            return -1

if __name__ == '__main__':
    s = Solution()
    print(s.strStr("mississippi", "issip"))