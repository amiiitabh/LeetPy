class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        lst=[]
        ans=0
        ans1=0
        for i in range(n+1):
            lst.append(i)
        for j in lst:
            ans+=j
        for k in nums:
            ans1+=k
        print(ans1)
        print(ans)
        return abs(ans1-ans)

        