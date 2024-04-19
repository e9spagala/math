def is_prime(n: int) -> bool:
    if n == 1:
        return False
    i = 2

    while i * i <= n:
        if n % i == 0:
            return False
        if n % (n // i) == 0:
            return False
        i += 1
    return True 


maxi = 10_001
LIMIT = maxi * maxi

def answer() -> int:
    temp = maxi
    for i in range(2, LIMIT + 1):
        if is_prime(i) == True:
            temp -= 1
        if temp == 0:
            return i
        
print(answer())



def solver(n: int) -> int:
    LIMIT = n * n
    temp = maxi
    for i in range(2, LIMIT + 1):
        if is_prime(i) == True:
            temp -= 1
        if temp == 0:
            return i


print(solver(10_001))