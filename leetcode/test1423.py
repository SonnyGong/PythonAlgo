class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        ans = ori_sum =  sum(cardPoints)
        this_turn_sum = 0
        k = len(cardPoints) - k
        if k == 0:
            return ori_sum
        for i,c in  enumerate(cardPoints):
            this_turn_sum += c
            if i < k - 1:
                continue
            # print(ans, this_turn_sum)
            ans = min(ans,this_turn_sum)
            # print(ans,this_turn_sum,'\n')
            this_turn_sum -= cardPoints[i - k + 1]
        return ori_sum - ans

class Solution1:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        ans = s = sum(cardPoints[-k:])  # 为方便下面 zip，改为先计算后 k 个数的和
        print(cardPoints[-k:])
        for x, y in zip(cardPoints, cardPoints[-k:]):
            print(x,y)
            s += x - y
            ans = max(ans, s)
        return ans

class Solution2:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        ans = s = sum(cardPoints[:k])
        for i in range(1, k + 1):
            print(cardPoints[-i],cardPoints[k - i])
            s += cardPoints[-i] - cardPoints[k - i]
            ans = max(ans, s)
        return ans


if __name__ == '__main__':
    s = Solution2()
    print(s.maxScore([1,2,3,4,5,6,1],k=3))