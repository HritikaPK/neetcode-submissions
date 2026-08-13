class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        # calculate distance of all points in List points to the origin using formula
        #(sqrt((x1 - x2)^2 + (y1 - y2)^2))
        distances = [0] * len(points)
        for i,(x,y) in enumerate(points):
            d = ((x-0)**2 + (y - 0)**2)**0.5
            distances[i] = (d,i)
        
       
        # min Heapify
        heapq.heapify(distances)
        

        #return ith k elements in distances
        for i in range(k):
            d,i = heapq.heappop(distances)
            result.append(points[i])


        return result
        