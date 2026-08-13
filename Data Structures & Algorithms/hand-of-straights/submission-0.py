class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        #check if we can create groupsize arrays out of hand
        if len(hand) % groupSize != 0:
           return False

        count = {}

        # create a hashmap 
        for i in range(len(hand)):
            count[hand[i]] = count.get(hand[i],0) + 1

        
        minheap = list(count.keys())
        heapq.heapify(minheap)

        #while minheap: get 1st element (min element)
        while minheap:
            first = minheap[0]
            # run a loop from min element to group size 
            # if element not in range in hashmap, return False
            for i in range(first, first + groupSize):
                if i not in count:
                    return False

                # check count in hashmap and reduce by 1
                count[i] -= 1
                # if element is min and count = 0; pop from heap
                if count[i] == 0:
                    if i != minheap[0]:
                        return False
                    heapq.heappop(minheap)
        return True

        