total_distance_in_miles=int(input("distance between you and the university in miles:"))
print("-----------------If you take the bus----------------\n ")
speed_in_mph= int(input("speed of bus in mph:"))
time = int(input("number of Bus stops:")) * int(input("spending time of bus in minutes:"))
time_taken_by_bus=((60/speed_in_mph)*total_distance_in_miles)+time
print(f"The bus will take {time_taken_by_bus} minutes to reach the destination.")
print ("-------------If you are jogging--------------\n")
speed1=int(input("enter your jogging speed during 1st mile in mph:"))
speed2=int(input("jogging seed during 2nd and third mile in mph:"))
speed3=int(input("jogging speed during the last mile in mph:"))
time_taken_by_jogging=(60/speed1)+(60/speed2)*2+(60/speed3)
print(f"you will take {time_taken_by_jogging} minutes to reach the destination.")
if time_taken_by_bus < time_taken_by_jogging:
    print("The bus will arrive first.")
elif time_taken_by_jogging==time_taken_by_bus:
    print("Both and will you will reach at same time.")
else:
    print("you will arrive first.")






