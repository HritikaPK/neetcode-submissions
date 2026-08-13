class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key in self.store:
            self.store[key].append([value,timestamp])
        else:
            self.store[key] = []
            self.store[key].append([value,timestamp])

        

    def get(self, key: str, timestamp: int) -> str:

        res = ""
        values = self.store.get(key,[])
        
        #bin search
        l = 0
        r = len(values)-1

        while l<=r:
            mid = (l+r)//2

            
            if values[mid][1] > timestamp:
                r = mid - 1
            elif values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1  
                       

        return res