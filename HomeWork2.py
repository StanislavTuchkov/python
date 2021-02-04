

data = ['game over', '08.03.2021', 751, True, 3.14]
data_0 = print(type(data[0]))
data_1 = print(type(data[1]))
data_2 = print(type(data[2]))
data_3 = print(type(data[3]))
data_4 = print(type(data[4]))


user_list = []
number_of_elements = int(input('Enter number if elements - '))
i = len(user_list)
print('Number of elements is: ' + str(number_of_elements))
while i < number_of_elements:
    user_list_element = input('Enter element (number or text) - ')
    user_list.append(user_list_element)
    i = len(user_list)

if (len(user_list) % 2) == 0:
    print(user_list[::2])
    print(user_list[1::2])
    user_list[::2], user_list[1::2] = user_list[1::2], user_list[::2]
    print(' '.join(user_list))
if (len(user_list) % 2) > 0:
    last_user_list = user_list.pop()
    user_list[::2], user_list[1::2] = user_list[1::2], user_list[::2]
    a = ' '.join(user_list)
    print(last_user_list)
    print(a + ' ' + last_user_list)


print('NEXT')

# season = dict(winter = [1, 2, 12],
#               spring = [3, 4, 5],
#               summer = [6, 7, 8],
#               autumn = [9, 10, 11])
# можно ли из словаря где ключ является списком вытаскивать значения списка используя ключ и индекс соответствующего скписка?

month = []
for i in range(1, 13):
    month.append(i)
user_month = int(input('Enter pls a number of the month - '))
month.append(user_month)
autumn = month[8:11:1]
spring = month[2:5:1]
summer = month[5:8:1]
del month[2:11] # не могу понять почему список не останавливается на 12 при применении метода del???? Голова увеличилась в 2 раза)))
winter = month
if user_month == autumn[0] or user_month == autumn[1] or user_month == autumn[2]:
    print('Autumn')
if user_month == winter[0] or user_month == winter[1] or user_month == winter[2]:
    print('Winter')
if user_month == spring[0] or user_month == spring[1] or user_month == spring[2]:
    print('Spring')
if user_month == summer[0] or user_month == summer[1] or user_month == summer[2]:
    print('Summer')


print('NEXT')

season_data = {1 : 'Winter', 2 : 'Spring', 3 : 'Summer', 4 : 'Autumn'}
user_month_dict = int(input('Enter months number - '))
if user_month_dict == 1 or user_month_dict == 2 or user_month_dict == 12:
    print(season_data.get(1))
if user_month_dict == 3 or user_month_dict == 4 or user_month_dict == 5:
    print(season_data.get(2))
if user_month_dict == 6 or user_month_dict == 7 or user_month_dict == 8:
    print(season_data.get(3))
if user_month_dict == 9 or user_month_dict == 10 or user_month_dict == 11:
    print(season_data.get(4))

print('NEXT')

user_words_enter = input('Enter any data using a space between them: ')
user_words_end = []
#print(user_words_enter.count(' '))
i = 1
for data in range(user_words_enter.count(' ') + 1):
    user_words_end = user_words_enter.split()
    #print(user_words_end)
    if (len(str(user_words_end))) <= 10:
        print(f' {i} {user_words_end [data]}')
        i += 1
        print(len(str(user_words_end)))
    else:
        print(f' {i} {user_words_end [data] [0:10]}')
        i += 1








