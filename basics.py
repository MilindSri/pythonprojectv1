day_hours = 24
week_days = 400
week_hours = day_hours * week_days
print(week_hours)

print("total week hours are : " + str(week_hours))

stringname = '123456'

print("Input the first number : ")

pattern = '*'
i = 0
j = 4
while(i < 4):
    j = j - i - 1
    while(j > i):
        print(j * " ")
        i = i + 1

