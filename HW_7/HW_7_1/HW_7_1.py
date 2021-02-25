from colorama import *
from prettytable import PrettyTable
t = PrettyTable()
list1 = [[1, 2, 3], [11, 22, 33], [111, 222, 333]]
list2 = [[4, 5, 6], [44, 55, 66], [444, 555, 666]]
# print(type(list1[0][0]))
t.add_row(list1)
t.add_row(list2)
print(t)

class Matrix:

    def __init__(self, list):
        self.list = list

    def __add__(self, other):
        sum = []
        for i in range(0, len(self.list)):
            sum.append([])
            for y in range(0, len(self.list[0])):
               sum[i].append(self.list[i][y] + other.list[i][y])
        return sum


matrix1 = Matrix(list1)
matrix2 = Matrix(list2)
sum_matrix = (matrix1 + matrix2)
print(Fore.RED + f'{sum_matrix[0]}' + Fore.GREEN + f'{sum_matrix[1]}' + Fore.BLUE + f'{sum_matrix[2]}')


    # a = list1[0]
    # b = a[0]
    # # print(type(b))
    # sum = [[],[],[]]
    # for i in range(0, len(list1)):
    #     a = list1[i][i] + list2[i][i]
    #     sum[i].append(a)
    # print(sum)
        # for x in range(0, 3):
        #     aa = a[x]
        #     bb = b[x]
        #     c = a[x] + b[x]
        #     # print(aa)
        #     # print(bb)
        #     print(c)
