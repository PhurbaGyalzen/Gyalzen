
def conversion(limit):
    a=0
    while a < (limit):
        if a%2==0:
            print(str(a),"even")
        else:
            print(str(a),"odd")
        a=a+1
conversion(3)