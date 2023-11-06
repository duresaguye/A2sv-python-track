class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_sqr_of_ditit(n):
            sum_squer = 0
            while n>0:

                digit = n%10
                sum_squer += digit**2
                n //=10
            return sum_squer
        seen_sum =set()
        while n !=1 and n not in seen_sum:
            seen_sum.add(n)
            n = sum_sqr_of_ditit(n)
           
            
            
            
        return n==1 

        
       

    
        
    




        