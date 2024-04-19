
def n_sum_squared(n: int) -> int:
     sum = n * (n + 1) // 2
     return sum*sum

def square_sum(n: int) -> int:
    return (n* (n + 1) * (2*n + 1)) // 6


def answer(n=100) -> int:
    
    return  n_sum_squared(n) - square_sum(n)

print(answer())


'''
we can use arithmetic progression to calculate sum of elements between p and q by:

sum(AP) = n(2a + (n - 1)* d) / 2

n = number of elements
a = starting number
d = common difference (i.e 1 in this case)

but I am going to solve it thorugh approach

'''
def solver(p: int, q:int) -> int:

    acutal_sum = n_sum_squared(q) - n_sum_squared(p)
    acutal_sum_squared = square_sum(q) - square_sum(p)
    return acutal_sum - acutal_sum_squared

print(solver(20, 100))
