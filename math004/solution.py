from typing import Union
def is_palindrome(n: int) -> bool:
    num:str = str(n)
    return num == num[::-1]
# Part A

## naive approah

def answer() -> int:
    last_palindrome: int = -1

    for i in range(100, 1000):
        for j in range(100, 1000):
            prod = i * j
            if is_palindrome(prod):
                last_palindrome = max(last_palindrome, prod)

    return last_palindrome

print(answer())

# Part B

def solver(n: int, p: int, q: int) -> Union[int, None]:
    
    low: int = 10**(n-1)
    high: int = low* 10
    last_palindrome = -1

    for i in range(low, high):
        for j in range(low, high):
            prod = i * j
            if  prod > p and prod < q and is_palindrome(prod):
                    last_palindrome = max(last_palindrome, prod)

    return last_palindrome

print(solver(4, 1000, 100000000 ))