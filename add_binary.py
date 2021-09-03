class Solution:
    def addBinary(self, a: str, b: str) -> str:

        
        len_a = len(a)
        len_b = len(b)
        max_len = max(len_a, len_b)
        num_a = 0
        
        for i,j in enumerate(a):
            num_a += int(j)*(2**(len_a - i - 1))
        
        for n,o in enumerate(b):
            num_a += int(o)*(2**(len_b - n - 1))
        str_bin = ""              
        for m in range(max_len+2,-1, -1):
            if num_a - 2**m >= 0:
                str_bin += str(1)
                num_a -= 2**m
                flag = 1
            elif str_bin != "":
                str_bin += str(0)
         
        if str_bin == "":
            return str(0)
        
        return str_bin
