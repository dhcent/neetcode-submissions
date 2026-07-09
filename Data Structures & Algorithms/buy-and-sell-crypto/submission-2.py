class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = -1
        L = 0
        R = 1
        cur_min = prices[0]
        while R < len(prices):
            # if right pointer price less than left pointer, update left pointer to there.
            if prices[R] < prices[L]:
                cur_min = prices[R]
                L = R
            else:
                max_profit = max(max_profit, prices[R] - prices[L])
            R += 1

        if max_profit == -1:
            return 0
        return max_profit