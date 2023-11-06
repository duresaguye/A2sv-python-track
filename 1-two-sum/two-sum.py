class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_with_indices = [(num, index) for index, num in enumerate(nums)]
        num_with_indices.sort(key=lambda x: x[0]) 
        left = 0
        right = len(num_with_indices) - 1
        
        while left < right:
            current_sum = num_with_indices[left][0] + num_with_indices[right][0]
            
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            elif current_sum == target:
                return [num_with_indices[left][1], num_with_indices[right][1]]

        return []
