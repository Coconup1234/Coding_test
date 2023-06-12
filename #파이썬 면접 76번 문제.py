class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = []
        result = []
        for i in range(len(nums)):
            
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            
            if queue[0] == i - k :
                queue.pop(0)
            if i >= k - 1:
                result.append(nums[queue[0]])
        return result