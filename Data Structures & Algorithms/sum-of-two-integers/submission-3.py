class Solution:
    def getSum(self, a: int, b: int) -> int:

        def add(a,b):

            while b!=0:
                carry=a&b
                a=a^b
                b= carry << 1

            return a

        def substract(a,b):
            while b!=0:
                borrow=(~a)&b
                a=a^b
                b= borrow << 1

            return a

        if a>=0 and b>=0:
            return add(a,b)
        if a<0 and b<0:
            return -add(abs(a),abs(b))

        pos = a if a>=0 else b
        neg = a if a<0 else b
        if pos >= abs(neg):
            return substract(pos,abs(neg))
        else:
            return -substract(abs(neg), pos)
        