f = open('file_4.txt')
dictionary = {'One': 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре' }
# print(f.read())
with open('file_4_translate.txt', 'w') as translate:
    with open('file_4.txt') as trans:
        for index, value in enumerate(trans):
           a = str(value.replace(value.split()[0], dictionary.get(value.split()[0])))
           translate.write(a)
# print(type(list))
# print(type(str_list))
# dictionary = {'One': 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре' }
# print(dictionary)
# for i in dictionary:
#     str_list = str_list.replace(i, dictionary[i])
# print(str_list)
#     x = str_list.split()
# print(f'{x[0]}  {x[1]}')
# print(type(a))
# b = a.replace()
# print(a)