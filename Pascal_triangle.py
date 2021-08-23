def pascal(llist):
    dummy = list()
    dummy.append(1)
    
    for i in range(len(llist)-1):
        dummy.append(llist[i] + llist[i+1])
    
    dummy.append(1)
    return dummy

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        count = 1  
        pas = list()
        pas.append(1)
        total = list()
        total.append(pas)
        if numRows == 1:
            return (total)        
        pas_list = list()
        pas_list.append(1)
        pas_list.append(1)
        total.append(pas_list)
 
        if numRows == 2:
            return total
        
        while count < numRows - 1:
            count += 1
            pas_list = pascal(pas_list)
            
            total.append(pas_list)
            print (pas_list)        
        return total
