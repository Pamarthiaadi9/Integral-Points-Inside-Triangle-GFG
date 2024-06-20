from math import sqrt, gcd

class Solution:
    def InternalCount(self, p, q, r):
        x1, y1 = p[0], p[1]
        x2, y2 = q[0], q[1]
        x3, y3 = r[0], r[1]
        A = self.area(x1, y1, x2, y2, x3, y3)
        b1 = self.boundry(x1, y1, x2, y2)
        b2 = self.boundry(x1, y1, x3, y3)
        b3 = self.boundry(x3, y3, x2, y2)
        B = b1 + b2 + b3 + 3
        return ( A - B + 2) // 2
        
    
    def boundry(self, x1, y1, x2, y2):
        if x1 == x2:
            return abs(y1 - y2) - 1
        elif y1 == y2:
            return abs(x1 - x2) - 1
        
        return gcd(abs(x1 - x2), abs(y1 - y2)) - 1
        
        
    
    def area(self, x1, y1, x2, y2, x3, y3):
        return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
