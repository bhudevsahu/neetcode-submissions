class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -1 * num)

        i = 1
        while i < k:
            heapq.heappop(heap)
            i += 1
        
        return -1 * heap[0]