class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        for num in nums:
            map[num] += 1

        heap = []
        for n in map.keys():
            heapq.heappush(heap, (map[n], n))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        

        return result