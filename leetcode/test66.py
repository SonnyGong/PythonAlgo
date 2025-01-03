class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits[-1] = digits[-1] + 1
        low_pointer = len(digits) - 1
        while low_pointer > 0:
            if digits[low_pointer] > 9:
                digits[low_pointer - 1] += (digits[low_pointer] // 10)
                digits[low_pointer] = (digits[low_pointer] % 10)


            low_pointer -= 1
        if digits[0] > 9:
            digits.insert(0, digits[0] // 10)
            digits[1] = (digits[1] % 10)

        return digits

class Solution_PUBLIC:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                for j in range(i + 1, n):
                    digits[j] = 0
                return digits

        # digits 中所有的元素均为 9
        return [1] + [0] * n

if __name__ == '__main__':
    s = Solution_PUBLIC()
    print(s.plusOne([9,4,4,4]))