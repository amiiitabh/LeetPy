class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num <2:
            return True
        
        low=0
        high=num//2
        
        while(high >=low):
            mid=(high+low)//2
            sq=int(mid*mid)
            if sq==num:
                return True
            elif sq>num:
                high=mid-1
            else:
                low=mid+1
        return False
                

        

        
        