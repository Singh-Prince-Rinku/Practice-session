class Solution:
  def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
    count = [0] * n

    meetings.sort()

    occupied = []
    RoomID = [i for i in range(n)]
    heapq.heapify(RoomID)

    for Begnings, end in meetings:
      while occupied and occupied[0][0] <= Begnings:
        heapq.heappush(RoomID, heapq.heappop(occupied)[1])
      if RoomID:
        roomId = heapq.heappop(RoomID)
        count[roomId] += 1
        heapq.heappush(occupied, (end, roomId))
      else:
        newStart, roomId = heapq.heappop(occupied)
        count[roomId] += 1
        heapq.heappush(occupied, (newStart + (end - Begnings), roomId))

    return count.index(max(count))