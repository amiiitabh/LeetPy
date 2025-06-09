class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lst=[]
        for i in nums:
            if i == val:
                continue
            else:
                lst.append(i)
        nums.clear()
        for  i in lst:
            nums.append(i)
