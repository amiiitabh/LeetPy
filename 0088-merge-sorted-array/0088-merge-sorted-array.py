class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        lst=[]
        for i in nums1[0:m]:
            lst.append(i)
        for j in nums2[0:n]:
            lst.append(j)
        lst.sort()
        nums1.clear()
        for k in lst:
            nums1.append(k)
        return nums1
        
        