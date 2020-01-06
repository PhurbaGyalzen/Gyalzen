def con():
    a=0
    for i in range (3,21):
        if i %3==0 or i % 5==0:
            i=a+i
            a=i
    return a
print(con())



