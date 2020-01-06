number_1=int(input('number_1:'))
number_2=int(input('number_2:'))
number_3=int(input('number_3:'))
if number_3 > number_2 and number_3 > number_1:
    print(f"{number_3} is greatest.")
elif number_2 > number_3 and number_2 > number_1:
    print(f"{number_2} is greatest.")
elif number_1 > number_2 and number_1 > number_3:
    print(f"{number_1} is greatest.")
