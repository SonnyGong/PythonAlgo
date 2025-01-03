# class Solution:
#     def mySqrt(self, x: int) -> int:
#         left_num = 0
#         right_num = x
#         while left_num <= right_num:
#             middle_num = (left_num + right_num) /2
#             if middle_num * middle_num > x:
#                 right_num = middle_num - 0.001
#             elif middle_num * middle_num < x:
#                 left_num = middle_num + 0.001
#             elif middle_num * middle_num == x:
#                 return int(middle_num)
#
#         return int(left_num)

# if __name__ == '__main__':
#     s = Solution()
#     print(s.mySqrt(8))