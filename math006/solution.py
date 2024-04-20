
def n_sum(n: int) -> int:
     sum = n * (n + 1) // 2
     return sum

def square_sum(n: int) -> int:
    return (n* (n + 1) * (2*n + 1)) // 6


def answer(n=100) -> int:
    
    sum_squared =  (n_sum(n))**2

    return sum_squared - square_sum(n)

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

    sum_squared = (n_sum(q) - n_sum(p - 1))**2

    squared_sum = square_sum(q) - square_sum(p - 1)
    # print(n_sum(q), n_sum(p), sum_squared, squared_sum)
    return sum_squared - squared_sum

print(solver(1, 100))



