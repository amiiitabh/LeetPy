class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posi=[];neg=[]
        k=len(nums)
        for i in nums:
            if i >=0:
                posi.append(i)
            elif i<0:
                neg.append(i)
        nums.clear()
        for j in range(k//2):
            nums.append(posi[j])
            nums.append(neg[j])
        return nums


        