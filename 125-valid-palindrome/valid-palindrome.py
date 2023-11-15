class Solution:
    def isPalindrome(self, s: str) -> bool:
        result =""
        for i in s:
            if i.isalnum():
                result+=i
        k=result.lower()
        if k[::-1]==k:
            return True
        else:
            return False 