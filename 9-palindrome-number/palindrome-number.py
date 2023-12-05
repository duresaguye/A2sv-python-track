class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and  x != 0):
            return False
        reversed_half  = 0
        while x > reversed_half:
            reversed_half =  reversed_half *10 + x%10
            x//=10
        return x== reversed_half or x == reversed_half//10
       


    """ y = str(x)
        left = 0
        right = len(y)-1
        while left < right :
            if y[left] != y[right]:
                return False
            left +=1
            right -=1
        return True 

    """