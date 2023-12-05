class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        left = 0
        right = len(y)-1
        while left < right :
            if y[left] != y[right]:
                return False
            left +=1
            right -=1
        return True 

        