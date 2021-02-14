from Random_number import list
print(list)
# a = []
# for index, value in enumerate(list):
#     if list[index] > list[index-1]:
#         print(value)

new_list = [el for index, el in enumerate(list) if list[index - 1] < list[index]]
print(new_list)
# вставить аргумент (el) с порядкковым номером (index), полученным из enumerate, если аргумент предстоящий
# \ (index - 1) меньше проверяемого аргумента
# print(list)






