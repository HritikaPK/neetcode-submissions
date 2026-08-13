class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # create a minheap
        self.minHeap = nums
        self.k = k

        # heapify 
        heapq.heapify(self.minHeap)

        # k elements in minheap - rest we will pop
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        # user can add elements -> push to our existing hyeap
        heapq.heappush(self.minHeap, val)

        # if no. of elemnts > k then pop
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]
        

        
          
