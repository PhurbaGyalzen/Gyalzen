a=int(input('enter a number.'))
def fizz_buzz():
    if a%3==0:
        return "Fizz"
    elif a%5==0:
        return "Buzz"
    elif a%3 and a%5==0:
        return "Fizzbuzz"
    else:
        return a
print(fizz_buzz())
