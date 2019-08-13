class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c = ""
        carry = 0
        if len(a) > len(b):
            a,b = b,a
        for i in range(len(a)-1,-1,-1):
            bit = int(a[i])+int(b[i+len(b)-len(a)])+carry
            c = str(bit%2) +c
            carry = int(bit/2)
        for i in range(len(b)-len(a)-1,-1,-1):
            bit = int(b[i])+carry
            c = str(bit%2) +c
            carry = int(bit/2)
        if carry ==1:
            c = "1"+c
        return c