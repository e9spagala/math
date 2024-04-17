from typing import List, Dict

def isPrime(n: int) -> bool:
    i: int = 2
    count: int = 0
    while i * i <= n:
        if n % i == 0:
            count += 1
        #  mitigating duplicate factors
        if n / i != i:
            count += 1
        if count > 2:
            return False
    
    return False if count > 2 else True

LIMIT: int = 10_000_000 # assuming 10^7 is the max limit for the given input
primes: List[bool] = [True for _ in range(LIMIT + 1)]
primes[0] = False
primes[1] = False

# Sieve of Eratosthenes
for i in range(2, LIMIT + 1):
    if primes[i] == False:
        continue
    # if the value is prime then mark the factors of those numbers as false
    if isPrime(primes[i]) == True:
        for j in range(i + i, LIMIT + 1, i):
            primes[j] = False

# Part A

inp: List[int] = [600,851,475,143]

def answer() -> Dict[int, int]:
    max_primes: Dict[int, int] = {}
    for ele in inp:
        max_prime = 2
        i = 2
        while i * i <= ele:
            if ele % i == 0:
                if primes[i] == True:
                    max_prime = max(max_prime, i)
                # if this is not a duplicate factor then check for this too
                other_factor = ele // i
                if other_factor // i != i:
                    if primes[other_factor] == True:
                        max_prime = max(max_prime, other_factor)
                
            i += 1
        max_primes[ele] = max_prime

    return max_primes

ans: Dict[int, int] = answer()

for key, val in ans.items():
    print(f'Maximum prime factor of {key}: {val}')


# Part B


def solver(n: int) -> int:
    max_prime = 2
    i = 2
    while i * i <= n:
        if n % i == 0:
            if primes[i] == True:
                max_prime = max(max_prime, i)
            # if this is not a duplicate factor then check for this too
            other_factor = n // i
            if other_factor // i != i:
                if primes[other_factor] == True:
                    max_prime = max(max_prime, other_factor)
            
        i += 1
    return max_prime


print(solver(203))
