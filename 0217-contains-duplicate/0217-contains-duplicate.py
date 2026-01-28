class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ss=set()
        for i in nums:
            if i in ss:
                return True
            ss.add(i)
        return False