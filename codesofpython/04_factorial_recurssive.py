def factorial_recur(n):
    if n==0 or n==1:
        return 1
    return n * factorial_recur(n-1)

f = factorial_recur(5)
print(f)























def factorial_re(n):
    if n==0 or n==1:
        return 1
    return(n*factorial_re(n-1))

f = factorial_re(6)
print(f)