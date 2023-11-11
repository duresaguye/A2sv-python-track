class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        reversed1 = int(str(num)[::-1]) if num>=0 else -int(str(-num)[::-1])
        reversed2 = int(str( reversed1)[::-1]) if  reversed1>=0 else -int(str(- reversed1)[::-1])
        if  reversed2 ==num:
            return True
        return False
        

        