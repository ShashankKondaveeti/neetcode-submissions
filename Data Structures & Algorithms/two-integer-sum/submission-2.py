class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements: dict[int, int] = {}
        for i in range(len(nums)):
            complement: int = target - nums[i]
            if complement in complements:
                return [complements[complement], i]
            complements[nums[i]] = i