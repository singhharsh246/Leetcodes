class Solution:
    
    def sum_squares(self, n:int) -> int:
        num = list(str(n))    
        target = sum(list(int(i)*int(i) for i in num))        
        return (target)
    
    
    def isHappy(self, n: int) -> bool:        
        target = self.sum_squares(n)
        
        flag = list()
        while True:
            if target == 1:
                    return True
            if target in flag:
                return False
            flag.append(target)
            target = self.sum_squares(target)
