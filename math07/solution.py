
maxi = 1_000_000
LIMIT = maxi * maxi

prime = [True for _ in range(LIMIT + 1)]

prime[0] = False
prime[1] = False

for i in range(2, LIMIT + 1):
    if prime[i] == True:
        for j in range(i * i, LIMIT + 1, i ):
            prime[j] = False

def answer() -> int:
    temp = maxi
    for i in range(2, LIMIT + 1):
        if prime[i] == True:
            temp -= 1
        if temp == 0:
            return i
        
print(answer())



def solver(n: int) -> int:
    LIMIT = n * n
    temp = maxi
    for i in range(2, LIMIT + 1):
        if prime[i] == True:
            temp -= 1
        if temp == 0:
            return i


print(solver(10_001))