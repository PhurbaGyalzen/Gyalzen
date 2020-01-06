number=int(input("num:"))
for div in range(2,number):

        if number%div ==0:
            print('not prime')
            break
else:
    print("prime")
