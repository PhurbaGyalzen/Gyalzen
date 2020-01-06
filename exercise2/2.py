maths=int(input('maths:'))
science=int(input('science:'))
physics=int(input('physics:'))
optional_maths=int(input('optional_maths:'))
Total=maths+science+physics+optional_maths
percentage=Total/4
print(f'Total:{Total}')
print(f'percentage:{percentage}')
if percentage >=70:
    print('Grade:Distinction.')
elif percentage < 70 and percentage >=60:
    print('Grade:first.')
elif percentage >=40:
    print('Grade:pass.')
else:
    print('Grade:fail.')

