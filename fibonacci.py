import timeit


stmt_closure = """
def fibonacci():
    res = [0, 1]

    def get_value(n):
        if len(res) > n:
            return res[n]

        prev, cur = res[-2], res[-1]
        while len(res) <= n:
            prev, cur = cur, cur + prev
            res.append(cur)
        return res[-1]

    return get_value
f = fibonacci()
f(40)
"""


stmt_recursion = """
import functools
@functools.lru_cache
def recursion_fibonacci(n):
    if n <= 1:
        return n
    return recursion_fibonacci(n-1) + recursion_fibonacci(n-2)
recursion_fibonacci(40)
"""


print(timeit.timeit(stmt_closure, number=10))
print(timeit.timeit(stmt_recursion, number=10))
