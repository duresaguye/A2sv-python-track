class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        brute force approach
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i]==nums[j] and i != j and abs(i-j)<=k:
                    return True
        return False"""
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True 
            seen.add(nums[i])
            if len(seen)>k:
                seen.remove(nums[i - k])
        return False
            

       

        