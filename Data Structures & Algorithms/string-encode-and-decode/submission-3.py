class Solution:

    def encode(self, strs: List[str]) -> str:

        # "#Hello","World"
        
        send = ""
        for s in strs:
            send += str(len(s)) + "#" + s #  "5#Hello"
        
        # "5#Hello5#World"
        return send

    def decode(self, s: str) -> List[str]:
        # "5#Hello5#World"
        #  ij 
        res = []
        i=0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
        return res

