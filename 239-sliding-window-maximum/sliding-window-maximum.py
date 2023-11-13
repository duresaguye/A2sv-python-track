from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        result = []
        window_indices = deque()

        for i in range(len(nums)):
            # Remove indices outside the current window
            while window_indices and window_indices[0] < i - k + 1:
                window_indices.popleft()

            # Remove indices of smaller elements from the back
            while window_indices and nums[i] > nums[window_indices[-1]]:
                window_indices.pop()

            # Add the current index to the deque
            window_indices.append(i)

            # If the window has reached its size, add the maximum to the result
            if i >= k - 1:
                result.append(nums[window_indices[0]])

        return result
