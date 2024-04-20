# How do you know the ith prime lies in a certain range in order to find the seive length.

maxi = 15_485_863

LIMIT = maxi 

prime = [True for _ in range(LIMIT + 1)]

prime[0] = False
prime[1] = False



def answer() -> int:
    t = 1_000_000
    for i in range(2, LIMIT + 1):
        if prime[i] == True:
            t -= 1
            if t == 0:
                return i
            for j in range(i * i, LIMIT + 1, i ):
                prime[j] = False
            
print(answer())



def solver(n: int) -> int:
    
    temp = n
    for i in range(2, LIMIT + 1):
        if prime[i] == True:
            temp -= 1
        if temp == 0:
            return i


print(solver(10_001))