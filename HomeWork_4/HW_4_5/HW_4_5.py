from functools import reduce
from Random_number import list
print(list)
new_list = reduce(lambda a, b: a * b, [value for index, value in enumerate(list) if value % 2 == 0])
print(new_list)
