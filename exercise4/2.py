print("""press 1 for celcious to faranhite
press 2 for faranhite to celcious.""")
inp=input('>')
if inp=="2":
    faranhite=int(input("faranhite:"))
    c=(5/9)*(faranhite-32)
    print(f"{faranhite} faranhite is equal to {c} celcious.")
elif inp=="1":
    celcious=int(input("celcious"))
    f=((celcious+32)*9)/5
    print(f"{celcious} celcious is equal to {f} faranhite.")

