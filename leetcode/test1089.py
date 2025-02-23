from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr) #数组总长
        zeros = arr.count(0)  # 统计零的个数
        i = n - 1  # 原数组的最后一个索引
        j = n + zeros - 1  # 新数组的最后一个索引

        while i >= 0: #将原数组从后往前遍历直到索引为0，先看第①和第②步
            if j < n: #直到新数组和原来的旧数组一样长
                arr[j] = arr[i]  #就将需要返回的数组的最后一个数和复写后的最后一个数相等
            if arr[i] == 0:  #如果这个数字是0或者倒数第一个数为0
                j -= 1  #就将需要返回的数组再减一
                if j < n:  #如果小于总长（这样就能规避最后一个数字是0的情况）
                # print(i,j)
                    arr[j] = 0  #赋零
            i -= 1   #①旧数组和新数组一起减一
            j -= 1   #①旧数组和新数组一起减一
        print(arr)

if __name__ == '__main__':
    sol = Solution()
    sol.duplicateZeros([1,0,2,3,0,4,5,0])