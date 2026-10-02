class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l=[]
        for a in range(1,n+1):
            if(a%3==0 and a%5==0):l.append("FizzBuzz")
            elif(a%3==0):l.append("Fizz")
            elif(a%5==0):l.append("Buzz")
            else:l.append(str(a))
        return l    
    

        