class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        longest = ""

        for c in range(len(s)):
            
            left, right = c, c
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(longest):
                    longest = s[left:right + 1]
                left -= 1
                right += 1

            
            left, right = c, c + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(longest):
                    longest = s[left:right + 1]
                left -= 1
                right += 1

        return longest
