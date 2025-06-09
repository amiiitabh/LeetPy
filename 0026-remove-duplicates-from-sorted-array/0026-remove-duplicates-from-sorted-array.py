class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        st=set(nums)
        nums.clear()
        for i in st:
            nums.append(i)
        nums.sort()
        