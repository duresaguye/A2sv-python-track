class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        """
        using brute force
        for i in range(len(nums)):
            left_sum = 0
            for j in range(i):
                left_sum=left_sum+nums[j]
            right_sum=0
            for j in range(i+1,len(nums)):
                right_sum = right_sum+nums[j]
            if left_sum==right_sum:
                return i
        return -1
        # using perfix sum and single loop
        perfix_sum =[0]*len(nums)
        perfix_sum[0] = nums[0]
        for i in range(1,len(nums)):
            perfix_sum[i]=perfix_sum[i-1]+nums[i]
        total_sum = perfix_sum[len(nums)-1]
        for i in range(len(nums)):
            left_sum = perfix_sum[i]-nums[i]
            right_sum=total_sum- perfix_sum[i]
            if left_sum == right_sum:
                return i
        return -1
        time complexity = O(n)
           space complexity =o(n)
        """
        #using online single loop
        #more effecent solution
        total_sum = 0
        left_sum = 0
        for i in range(len(nums)):
            total_sum = total_sum +nums[i]
        for i in range(len(nums)):
            right_sum=total_sum-left_sum-nums[i]
            if right_sum==left_sum:
                return i
            left_sum=left_sum+nums[i]
        return -1


        