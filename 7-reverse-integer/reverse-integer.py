class Solution:
    def reverse(self, x: int) -> int:
        reverse_x = int(str(x)[::-1]) if x >= 0 else -int(str(-x)[::-1])
        if reverse_x <= -2**31 or reverse_x>=2**31:
            return 0
        return reverse_x
       
    
        
        