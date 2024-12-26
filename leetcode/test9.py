class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        elif x == 0:
            return True
        else:
            reverse_num = 0
            while x > reverse_num:
                reminder = x % 10
                reverse_num = reverse_num * 10 + reminder
                x = x // 10
            if x == reverse_num or reverse_num // 10 == x:
                return True
            return False


if __name__ == '__main__':
    test = Solution()
    print(test.isPalindrome(121))