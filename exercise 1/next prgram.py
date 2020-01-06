#wap to take user
'''list =[]
s=0
odd=[]
for i in range(5):
    number=int(input("enter number"))
    list.append(number)
    s=s+number
print(list)
print(s)
#wap to take a list consists of 10 numbers and find greatst,smaallest ,list of odd number.'''
num=[]
odd=[]
for i in range(10):
    number=int(input("numbers"))
    num.append(number)
    if not (number %2 ==0):
        odd=odd+[number]
print(num)
print(odd)

