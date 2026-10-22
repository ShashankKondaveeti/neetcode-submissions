class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        total = 1
        total_without_zeroes = 1
        num_zeroes = 0
        for val in nums:
            total *= val
            if val == 0:
                num_zeroes += 1
            else:
                total_without_zeroes *= val
        for val in nums:
            if val == 0 and num_zeroes == 1:
                output.append(total_without_zeroes)
            elif val == 0:
                output.append(0)
            else:    
                output.append(total // val)
        return output 
            