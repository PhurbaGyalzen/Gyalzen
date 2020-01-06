a=int(input("physics:"))
b=int(input("maths:"))
c=int(input("chemistry:"))
d=int(input("engish:"))
total=a+b+c+d
print("total marks:",total)
per=(total/4)
print("total per:", per)
if per >= 70:
    print("your grade is distinction")
elif per>=60 and per<70:
    print("your grade is first division")
elif per >= 40 and per < 60:
    print("you have pass grade.")
elif per < 40:
     print("you are fail.")
