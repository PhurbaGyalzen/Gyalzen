#wap to take a user input of 10 number in a list and print them in assending order
#prime number.
num=[5,4,3,1,2]
i=0
while i < 5:
    j=0
    while j<4:
        if num[j] > num[j+1]:
            temp=num[j]
            num[j]=num[j+1]
            num[j+1]=temp
        j=j+1
    i=i+1
print(num)