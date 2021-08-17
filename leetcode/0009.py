class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x[0] == '-':
            return False
        size = len(x)
        if size == 1:
            return True
        if size == 2:
            if x[0] == x[1]:
                return True
            else:
                return False
        print (size)
        if size % 2 == 0:
            print ('f1')
            for z in range (int(size/2)):
                if x[z]!= x[-1-z]:
                    return False
                else:
                    pass
        else:
            for z in range (int(size/2 -0.5)):
                if x[z]!= x[-1-z]:
                    return False
                else:
                    pass
        return True