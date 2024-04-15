from typing import List
# Part A
def sum_of_multiples() -> int:
    return sum([i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0])

print(sum_of_multiples())

# Part B
def sum_of_multiples(lst:List[int]=[3, 5, 12], low:int=400, high:int=1842) -> int:
    sum = 0
    for i in range(low, high + 1):
        for j in lst:
            if i % j == 0:
                sum += i
                break
    return sum

print(sum_of_multiples())

