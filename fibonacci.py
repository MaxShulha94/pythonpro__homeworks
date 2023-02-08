def fib():
    buf = []
    prev, curr = 0, 1

    def get_next(n):
        nonlocal prev, curr
        while len(buf) < n:
            prev, curr = curr, prev + curr
            buf.append(curr)
        if len(buf) >= n:
            return buf[n]

        res = buf[-1]
        for i in range(len(buf), n):
            prev, curr = curr, prev + curr
            buf.append(curr)

        return res

    return get_next


x = fib()
print(x(4))
