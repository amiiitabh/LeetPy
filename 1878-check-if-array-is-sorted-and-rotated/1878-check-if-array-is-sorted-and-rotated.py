class Solution:
    def check(self, nums: List[int]) -> bool:
        lst = sorted(nums)
        k = len(nums)
        for i in range(k):
            if lst == nums:
                return True
            else:
                j = nums.pop()
                nums.insert(0, j)
        return False
            

