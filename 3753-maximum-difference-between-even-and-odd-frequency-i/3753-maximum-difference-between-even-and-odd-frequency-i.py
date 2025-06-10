class Solution:
    def maxDifference(self, s: str) -> int:
        st=set()
        for i in s:
            st.add(i)
        lst=[]
        for i in st:
            lst.append(s.count(i))
        even=[];odd=[]
        for i in lst:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        k=min(even)
        j=max(odd)
        return j-k

