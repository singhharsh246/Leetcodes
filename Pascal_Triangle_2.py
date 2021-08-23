
        def pascal(llist):
    dummy = list()
    dummy.append(1)

    for i in range(len(llist)-1):
        dummy.append(llist[i] + llist[i+1])

    dummy.append(1)
    return dummy

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        count = 1
        pas_list = list()
        pas_list.append(1)
        
        if rowIndex == 0:
            return pas_list

        pas_list.append(1)
        
        if rowIndex == 1:
            return pas_list

        while count < rowIndex:
            count += 1
            pas_list = pascal(pas_list)
        return pas_list
