class Solution:
    def maxSum(self, nums: List[int]) -> int:
        def max_digit(number):
            return max(map(int, str(number)))

        max_digits = [max_digit(num) for num in nums]
        max_sum = float('-inf')
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if max_digits[i] == max_digits[j]:
                    current_sum = nums[i] + nums[j]
                    max_sum = max(max_sum, current_sum)
        return max_sum if max_sum != float('-inf') else -1

        
        

       

            
        