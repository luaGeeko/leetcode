class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # edge case where the len of array and k window size is same
        if len(nums) == k:
            return sum(nums) / k
        subarray_window_sum = sum(nums[:k])
        max_sum = subarray_window_sum
        # loop fo next k windows
        for i in range(k, len(nums)):
            # subtract the first value of the previous window from the new value which will get add, as windows moves to right with stride 1
            subarray_window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, subarray_window_sum)
        return max_sum / k