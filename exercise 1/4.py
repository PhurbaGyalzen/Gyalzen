N=int(input("enter the number of minutes passed since midnight:"))
if N >= 1440:
    hours = ((N // 60)//24)-1
    minutes = N % 60
    print(str(hours)+":"+ str(minutes))
else:
    hours = (N // 60)
    minutes = N % 60
    print(str(hours)+":"+str(minutes))
