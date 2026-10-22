class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0  
        n_set = set(nums)
        total = 0
        longest = 0

        for val in n_set:
            if (val - 1) in n_set:
                continue
            else:
                while (val + 1) in n_set:
                    val += 1
                    total += 1
                if total > longest:
                    longest = total
                total = 0
        return longest + 1

            


        