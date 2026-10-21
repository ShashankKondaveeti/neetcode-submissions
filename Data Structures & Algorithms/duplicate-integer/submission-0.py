class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        
        for val in nums:
            if val not in my_set:
                my_set.add(val)
            else:
                return True
        return False
            