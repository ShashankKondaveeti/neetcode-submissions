import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        heap = []
        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)
        return heapq.nlargest(k, frequency.keys(), key = lambda num: frequency[num])
        