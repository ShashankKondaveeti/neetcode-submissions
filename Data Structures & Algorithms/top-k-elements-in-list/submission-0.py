import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        heap = []
        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)
        # for key in frequency:
        #     if len(heap) == 7:
        #         if 
        #         heap.heappush(frequency[key], key)
        return heapq.nlargest(k, frequency.keys(), key = lambda num: frequency[num])
        

#heapq.nlargest(k, nums, key = lambda num: frequency[num])