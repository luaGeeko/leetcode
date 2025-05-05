class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference_tracker = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in difference_tracker:
                # we have found the solution
                return [difference_tracker[diff], i]
            difference_tracker[nums[i]] = i