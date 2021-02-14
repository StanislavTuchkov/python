list = range(20, 240)
# print(list)
# a = []
# b = []
# for value in list:
#     if value % 20 == 0:
#        a.append(value)
#     if value % 21 == 0:
#         b.append(value)
# print(a)
# print(b)
a = [value for index, value in enumerate(list) if value % 20 == 0 or value % 21 == 0]
print(a)
# можно ли в одну строку прописать решение, чтобы на выходе было отдельно две переменные с кратным 20 и отдельно
# \ кратным 21

