# Complexity - T: O(nlogn), S: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num, count in freq.items():
            heapq.heappush(heap, [count, num])
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(len(heap)):
            res.append(heapq.heappop(heap)[1])

        return res