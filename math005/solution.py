
def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    return gcd(b % a, a)

def answer() -> int:
    arr = [i for i in range(1, 21)]
    lcm = 1
    for i in arr:
        lcm = lcm*i//gcd(lcm, i)
    return lcm

print(answer())

def solver(p: int, q: int) -> int:
    arr = [i for i in range(p, q + 1)]
    lcm = 1

    for i in arr:
        lcm = lcm * i // gcd(lcm, i)
    return lcm


print(solver(5, 10))