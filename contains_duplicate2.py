class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        dict_list = {}
        
        for i,j in enumerate(nums):
            if j not in dict_list.keys():
                dict_list[j] = []
                dict_list[j].append(i)
            else:
                dict_list[j].append(i)
            
        
        print(dict_list)
        for m, n in dict_list.items():
            if len(n) > 1:
                    for gh, jh in enumerate(n):
                        flag = gh+1
                        while flag < len(n):
                            
                            print(n[flag], n[gh], n)
                            if n[flag] - n[gh] <= k:
                                return True
                            else:
                                flag += 1
        return False
