# A program to find whether a person is eligible for vote or not
print("""''You have to fill all the following details
 to find whether you are eligible for the vote or not .''
                                      -- Government of nepal-""")
a = input("---------ENTER YOUR  NAME... ")
b = input("enter your last name..")

d = int(input("---------enter your age"))
e = input("-------------enter your country name")
f = ["nepal","Nepal","NEPAL"]
g = "sorry {1} {0}  your age is not valid for voting although you are a nepali citizen"
h = "sorry {0}  you are not a nepali citizen but you have a required age.."
i = "Sorry {0} you are not eligible for voting because your age and nationality doesnt reach the requirements.."
j = """***Congratulation {0}  you are eligible for voting. 
    Both your age and nationality are correct.***"""
if d < 18 and e in f :
    print(g.format(a,b))
elif d >= 18 and e not in f:
    print(h.format(a,b))
else:
    print(i.format(a,b))
if d >= 18 and e in f:
    print(j.format(a,b))







