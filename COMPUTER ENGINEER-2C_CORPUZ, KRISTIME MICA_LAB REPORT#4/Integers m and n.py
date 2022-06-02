def mult(m,n):
    if m == 0 or n == 0:
        return 0
    if n == 1:
        return m
    if m == 1:
        return n
    if m < 0 and n < 0:
        return mult(-m, -n)
    if n < 0:
        return -mult(m, -n)
    if m < 0:
        return -mult(-m, n)
    return m + mult(m, n - 1)

m = int(input())
n = int(input())
print (mult(m, n))