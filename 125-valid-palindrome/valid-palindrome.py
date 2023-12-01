class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for i in s:
            if i.isalnum():
                res +=i
        st="".join(res)
        ans = st.lower()
        return ans == ans[::-1]
          

        

        