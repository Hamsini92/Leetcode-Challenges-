class Solution:
    def isHappy(self, n):
         
            stop = {1}
            
            while n not in stop:
                stop.add(n)
                n = sum(int(x)**2 for x in str(n))
            
            return n==1
        
