
a = 1
b = 2
c = 3
print(a, b, c)

print('NEXT')

a = input('Введите первое число - ')
b = input('Введите втрое число - ')
c = input('Введите третье число - ')
print(a, b, c)

print('NEXT')

a = int(input('Введите время в секундах для конвертации в формат чч:мм:сс - '))
print('Конвертирую....')
hours = a // 3600
minutes = (a - hours * 3600) // 60
seconds = a - hours * 3600 - minutes * 60
print(f'{hours}ч:{minutes}м:{seconds}с')

print('NEXT')

n = input('Введите любое целое число - ')
sum_n_nn_nnn = int(n) + int(n+n) + int(n+n+n)
print(sum_n_nn_nnn)

print('NEXT')

number_a = int(input('Введите любое положительное целое число - '))
number_b = 1
number_c = number_a % number_b
print(f'остаток от первой операции - {number_c}')
while number_c <= 0:
    number_b = number_b + 1
    number_c = number_a % number_b
if number_c > 0:
    number_a = number_a - number_c
    print(number_c)
    print(f'знаменатель: {number_b}')
    print(f'наибольше число - {number_a}')

revenue = int(input('Пожалуйста, введите выручку Вашей компании ₽ - '))
expenses = int(input('Введите расходы за тот же период ₽ - '))
if revenue > expenses:
        print('Ваша компания работает хорошо! Так держать!')
else:
    print('Вам стоит предприянять меры для улучшения показателей прибыли Вашей компании!')
employee = int(input('Сколько сотрудников в Вашей компании? - '))
profit_per_employee = (revenue - expenses) // employee
if profit_per_employee <= 0:
    print(f'Убыток на каждого сотрудника составил - {profit_per_employee}₽')
else:
    print(f'Прибыль на каждого сотрудника сосатвила - {profit_per_employee}₽')

print('NEXT')

first_day = int(input('Сколько пробежал спортсмен в 1-й день км - '))
run_target = int(input('Введите целевой показатель тренировок км - '))
day_target = int(input('Введите целевой показатель по дням - '))
day = 0
day_text = 'дней' #Вопорс: как написать функцию, которая будет менять значение переменной (день, дней, дня)
                # в зависимости от последней цифры в целом числе и без учета разрядности: 1 - день, 21 - день, 2 - дня, 42 - дня и т.д.
if day_target < 5 and day_target > 1:
    day_text = 'дня'
elif day_target < 2:
    day_text = 'день'
else:
    day_target = day_target
# first_day_10 = first_day + first_day*0.1
while first_day < run_target:
    first_day = round((first_day + first_day * 0.1), 2)
    day += 1
    if first_day == run_target:
        break
    else:
        print(f'{day}-й день: {first_day}')
print(f'На {day}-й день спортсмен достиг целевого показателя в {run_target} км!')
if day >= day_target:
    print(f'Необходимо достичь показателя в {run_target} км за {day_target} {day_text}.')
    print(f'Следует лучше порабоать на тренироваках!')
else:
    print('Хорошая работа, чемпион!')



