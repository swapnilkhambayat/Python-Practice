print("Today's Date?")
day = input()
print("Breakfast calories?")
Bcal = int(input())
print('Lunch calories?')
Lcal = int(input())
print('Dinner calories?')
Dcal = int(input())
print('Snack calories')
Scal = int(input())
total_cal = Bcal + Lcal + Dcal + Scal
print('Calorie content for ' + day + ':' +  str(total_cal))