class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_list = list()
        strs_original = strs.copy()
        for i in range(len(strs)):
            strs[i] = sorted(strs[i])
        
        print("strs initial: " ,strs)
        print("original: ", strs_original)
        
        check = 0
        sub_list = list()
        while(check != len(strs)):
            for i in range(len(strs)):
                if strs[check] == strs[i]:
                    sub_list.append(strs_original[i])
                    print(sub_list) 
            check += 1
            if sub_list not in final_list:
                final_list.append(sub_list)
            print(final_list)
            sub_list = list()
        return final_list
        
    

