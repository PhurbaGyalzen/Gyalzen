Given_string=input(">")
final_string=""
for i in range(0,len(Given_string)+1,2):
    first_string=Given_string[i]
    initial_string=final_string+first_string
    final_string=initial_string
print(final_string)
