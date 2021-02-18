s = open('salary.txt')
a = s.readline()
total = []
with open('salary.txt') as a:
    for index, value in enumerate(a):
        c = value.split()
        total.append(c)
        # print(c)
        # for i in c:
        #     if i.isnumeric():
        #         if int(i) > 20000:
        #             print(i)
key_total = dict(total)
for key in key_total:
    key_total[key] = float(key_total[key])
    if key_total[key] > 20000:
        print(f'{key} {key_total[key]}₽')

# with open('3.txt', 'r', encoding='utf-8') as f:
#     employees_dict = {line.split()[0]: float(line.split()[1]) for line in f}
#     print(f'Average salary = {round(sum(employees_dict.values()) / len(employees_dict), 3)}\n'
#           f'Employees with salary less than 20k {[e[0] for e in employees_dict.items() if e[1] < 20000]}')
