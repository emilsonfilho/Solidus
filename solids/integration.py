def simpson(f, a, b, n):
    if n % 2 == 1:
        n += 1
    h = (b-a)/n
    
    res = f(a) + f(b)
    
    for i in range(1,n):
        xi = a + i * h
        multiplier = 4 if i % 2 == 1 else 2
        res += multiplier * f(xi)

    res *= h/3
    
    return res
    