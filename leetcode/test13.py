class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
        }
        roman_index_dict = {
            'I': ['V', 'X'],
            'X': ['L', 'C'],
            'C': ['D', 'M'],
        }
        return_num = 0
        single_roman_index = 0
        for _ in range(len(s)):
            if single_roman_index > len(s) - 1:
                return return_num

            this_roman_key = s[single_roman_index]
            if this_roman_key in roman_index_dict:
                if single_roman_index + 1 < len(s):
                    next_roman_key = s[single_roman_index + 1]
                    if next_roman_key in roman_index_dict[this_roman_key]:
                        return_num += (roman_dict[next_roman_key] - roman_dict[this_roman_key])
                        single_roman_index += 2
                    else:
                        return_num += roman_dict[this_roman_key]
                        single_roman_index += 1
                else:
                    return_num += roman_dict[this_roman_key]
                    single_roman_index += 1


            else:
                return_num += roman_dict[this_roman_key]
                single_roman_index += 1


        return return_num



if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("III"))