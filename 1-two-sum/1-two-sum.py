class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for idx in range(len(nums)):
            if dict.get(target - nums[idx],-1) != -1:
                return [dict[target - nums[idx]], idx]
            dict[nums[idx]] = idx