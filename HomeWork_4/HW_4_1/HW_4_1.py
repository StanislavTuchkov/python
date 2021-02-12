working_hours = 0
pay_for_hour = 100
total_salary = 0
prize = 1000
working_hours = int(input('Enter working hours - '))
if working_hours >= 12:
    total_salary = pay_for_hour * working_hours + prize
else:
    total_salary = pay_for_hour * working_hours
print(total_salary)