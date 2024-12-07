class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        temp = 0
        sym = 1
        if x < 0:
            x *= -1
            sym = -1
        
        xlen = len(str(x))
        
        for i in range(1, len(str(x))+1, 1):
            temp = (x % 10) * 10**(xlen-i)
            x = x // 10
            num += temp
            
        if num >= 2**31 -1:
            return 0
        
        return num * sym
