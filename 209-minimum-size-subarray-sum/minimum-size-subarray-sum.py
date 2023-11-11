class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """brute force soultion  
        n = len(nums)
        min_len = float('inf')

        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]

                if current_sum >= target:
                    min_len = min(min_len, j - i + 1)
                    break

        return 0 if min_len == float('inf') else min_len
                              """
        left,total =0,0
        res = float("inf")
        for right in range(len(nums)):
            total +=nums[right]
            while total >= target:
                res = min(right-left+1, res)
                total -=nums[left]
                left +=1
        return 0  if res ==float("inf") else res
            
       
            
                
                
            
                
                
            
        