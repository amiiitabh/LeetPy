class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lst=[]
        for i in nums:
            lst.append(i)
        lst.append(target)
        lst.sort()
        for i in range(len(lst)):
            if lst[i]==target:
                return i
                break;
            else:
                pass