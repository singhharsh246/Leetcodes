class Solution:
    def roman_num(self, target:int, flag:int, ld:str):
        temp_str = list()
        while target >= flag:
            temp_str.extend(ld)
            target = target - flag
        return temp_str
    
    
    def edge_cases(self, target, lower_limit:int, upper_limit:int, ld:str):   
        temp_str = list()
        if (lower_limit <= target <= upper_limit):
            temp_str.extend(ld)
            target -= lower_limit
        return target, temp_str
    
    
    def equality_edge_case(self, target:int, number:int, ld:str):
        if target == number:
            return 0, ld
        else:
            return target, []
    
    def intToRoman(self, num: int) -> str:
        str_num = list()
        str_num.extend(self.roman_num(num, 1000, "M"))
        num %= 1000
        
        num, temp_str = self.edge_cases(num, 400, 499, "CD")        
        str_num.extend(temp_str)
        num, temp_str = self.edge_cases(num, 900, 999, "CM")
        str_num.extend(temp_str)
        str_num.extend(self.roman_num(num, 500, "D"))
        num %= 500
        str_num.extend(self.roman_num(num, 100, "C")) 
        num %= 100
        
        num, temp_str = self.edge_cases(num, 40, 49, "XL")        
        str_num.extend(temp_str)
        num, temp_str = self.edge_cases(num, 90, 99, "XC")
        str_num.extend(temp_str)        
        str_num.extend(self.roman_num(num, 50, "L"))
        num %= 50
        
        
        num, temp_str = self.equality_edge_case(num, 4, "IV")
        str_num.extend(temp_str)
        num, temp_str = self.equality_edge_case(num, 9, "IX")
        str_num.extend(temp_str)
        
        
        str_num.extend(self.roman_num(num, 10, "X"))
        num %= 10
        
        num, temp_str = self.equality_edge_case(num, 4, "IV")
        str_num.extend(temp_str)
        num, temp_str = self.equality_edge_case(num, 9, "IX")
        str_num.extend(temp_str)
        
        str_num.extend(self.roman_num(num, 5, "V"))
        num %= 5
        
        num, temp_str = self.equality_edge_case(num, 4, "IV")
        str_num.extend(temp_str)
        num, temp_str = self.equality_edge_case(num, 9, "IX")
        str_num.extend(temp_str)
        
        str_num.extend(self.roman_num(num, 1, "I"))
        
        str_num = ("").join(i for i in str_num if i.isalnum())
        
        return str_num
