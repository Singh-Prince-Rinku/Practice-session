class Solution:
  def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
    minimum_Heap = []

    for i, (a, b) in enumerate(itertools.pairwise(heights)):
      k = b - a
      if k <= 0:
        continue
      heapq.heappush(minimum_Heap, k)
      if len(minimum_Heap) > ladders:
        bricks -= heapq.heappop(minimum_Heap)
      if bricks < 0:
        return i

    return len(heights) - 1