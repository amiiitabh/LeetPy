class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pivot=prices[0]
        x=0
        for i in prices[1:]:
            if i<pivot:
                pivot=i
            elif i-pivot>x:
                x=i-pivot
            else:
                pass
        return x
