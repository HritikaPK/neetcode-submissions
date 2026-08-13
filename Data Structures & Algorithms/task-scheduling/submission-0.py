class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # take count

        count = {}
        freq = []
        

        for item in tasks:
            count[item] = count.get(item,0) + 1
        print(count)

        for v in count.values():
            freq.append(v)

        # heapify freq
        freq = [-i for i in freq]
        heapq.heapify(freq)

        #create qyeye to track freq
        q = deque()
        time = 0
        #while cfreqount has numbers and queue has numbers
        while freq or q:
            time += 1
            if freq:
                num = heapq.heappop(freq) + 1
                if num: q.append([num,time+n])
            if q and q[0][1] == time:
                
                heapq.heappush(freq,q.popleft()[0])
            
        return time