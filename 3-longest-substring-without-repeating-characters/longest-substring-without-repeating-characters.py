class Solution(object):
    def lengthOfLongestSubstring(self, s):
        hashmap = {}
        start = 0
        length_string = 0
        for end in range(len(s)):
            if s[end] in hashmap and hashmap[s[end]]>=start:
                start = hashmap[s[end]] + 1
            hashmap[s[end]]=end
            length_string = max(length_string,end-start+1)
        return length_string
     

       