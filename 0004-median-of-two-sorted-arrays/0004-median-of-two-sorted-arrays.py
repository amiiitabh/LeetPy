class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst=[]
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        ans=0
        print(nums1)
        if len(nums1)%2==0:
            p=len(nums1)//2
            d=nums1[p-1]
            b=nums1[p]
            print(d,b)
            return (d+b)/2
        else:
            k=len(nums1)
            a=(k//2)
            return nums1[a]
        


