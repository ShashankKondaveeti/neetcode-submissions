import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        heap = []
        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)
        for key in frequency:
            if len(heap) == k:
                if frequency[key] > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (frequency[key], key))
            else:
                heapq.heappush(heap, (frequency[key], key))
        return [tup[1] for tup in heap]

        #return heapq.nlargest(k, frequency.keys(), key = lambda num: frequency[num])
        