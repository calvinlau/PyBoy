class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}
        for i in range(len(nums)):
            if nums[i] not in num_map:
                num_map[target - nums[i]] = i
            else:
                return num_map[nums[i]], i
        return -1, -1
