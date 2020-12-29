def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fast_fib(n, memo={}):

    if n==0 or n==1:
        return 1
    
    if n in memo:
        return memo[n]
    else:
        result = fast_fib(n-1) + fast_fib(n-2)
        memo[n] = result
        return result

print(fast_fib(120))