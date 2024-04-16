from typing import List, Union

# PART A
LIMIT = 4_000_000
def answer() -> None:
    
    
    
    f2: int = 1
    f3: int = 2
    total: int = 0
    while f2 <= LIMIT:
        if f2 & 1 == 0:
            total += f2
        f2, f3 = f3, f2 + f3
    print(total)

answer()

#PART B

def solver(start, end, even=False, odd=False) -> Union[None, int]:

    if start > end:
        return None
    
    if not even and not odd: 
        return []

    total: int = 0

    if even:
        f2: int = 1
        f3: int = 2
        while f2 <= end:
            if f2 >= start and f2 & 1 == 0:
                total +=f2
            f2, f3 = f3, f2 + f3

    if odd:
        f2: int = 1
        f3: int = 2
        while f2 <= end:
            if f2 >= start and f2 & 1 != 0:
                total +=f2
            f2, f3 = f3, f2 + f3
    return total

print(solver(2_000_000, 4_000_000, even=True, odd=False))



