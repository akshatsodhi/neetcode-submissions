class Solution:
    def isHappy(self, n: int) -> bool:
        a=str(n)

        while(n>=1):
            sum1=0
            for i in range(len(a)):
                b=int(a[i])*int(a[i])
                sum1=sum1+b
            n=sum1
            a=str(n)
        

            if n==1:
                return True
            if n==4:
                return False

        
            