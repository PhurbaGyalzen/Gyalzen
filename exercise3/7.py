def string():
    b=0
    c=0
    string='HelloH'
    for i in range(len(string)):
        if ord(string[i])>=97 and ord(string[i])<=122:
            a=1+b
            b=b+1
    print(f'There are {a} lowercase.')
    for i in range(len(string)):
        if ord(string[i])>=65 and ord(string[i])<=90:
            d=1+c
            c=c+1
    print(f'There are {d} uppercase.')
string()
