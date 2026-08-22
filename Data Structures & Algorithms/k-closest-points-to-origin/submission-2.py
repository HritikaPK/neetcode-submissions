class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # k closest points
        # 2-D array

        minHeap = []
        for point in points:
            x, y = point
            dist = math.sqrt((x**2)+(y**2))
            minHeap.append((dist,point))
        
        heapq.heapify(minHeap)
        res = []

        for i in range(k):
            dist, point = heapq.heappop(minHeap)
            res.append(point)

        return res
