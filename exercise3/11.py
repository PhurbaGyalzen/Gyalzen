# factorial using recursion.w
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
n=int(input('number:'))
print(factorial(n))
