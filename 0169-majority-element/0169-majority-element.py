class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        lst=[];st=set(nums)
        sorted(nums)
        for i in st:
            lst.append(nums.count(i))
        for  i in range(len(st)):
            j=lst.index(max(lst))
        lst2=list(st)
        return (lst2[j])
            
