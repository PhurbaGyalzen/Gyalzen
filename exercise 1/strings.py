print('To find the greatest number among 3 numbers.')
a=int(input('enter first number:'))
b=int(input('enter second number.'))
c=int(input('enter third number.'))
def high():
        if a>b and a>c:
            print(f'{a} is greatest.')
        elif b>a and b>c:
            print(f'{b} is greater.')
        elif c>a and c>b:
            print(f'{c} is greater.')
high()

