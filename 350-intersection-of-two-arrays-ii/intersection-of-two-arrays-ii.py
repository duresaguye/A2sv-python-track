

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        left = 0 
        nums1.sort()
        nums2.sort()
        right = 0
        ans = []
        while left<len(nums1) and right <len(nums2):
            if nums1[left]<nums2[right]:
                left+=1
            elif nums1[left]>nums2[right]:
                right+=1
            else:
                ans.append(nums1[left])
                left+=1
                right+=1
        return ans


        