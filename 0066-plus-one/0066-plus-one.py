class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''
        for i in digits:
            s=s+str(i)
        print(s)
        a=int(s)
        b=a+1
        lst=[]
        for j in str(b):
            lst.append(j)
        nums1=[]
        for i in lst:
            nums1.append(int(i))
        return nums1

        