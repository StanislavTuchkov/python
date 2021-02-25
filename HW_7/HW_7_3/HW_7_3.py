class Cell:

    def __init__(self, cell_numbers):
        self.number = cell_numbers


    def __add__(self, other):
        return self.number + other.number

    def __sub__(self, other):
        if (self.number - other.number) <= 0:
            print('ERROR! No cells in incubator!')
        else:
            return self.number - other.number

    def __mul__(self, other):
        return self.number * other.number

    def __truediv__(self, other):
        return self.number // other.number

    def make_oder(self, rows):
        print_row_cell = ''
        for i in range(self.number // rows):
            print_row_cell += f'{"*" * rows}  \n'
        print(print_row_cell + '*' * (self.number % rows))



cell1 = Cell(9)
cell2 = Cell(2)

print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell1.make_oder(2))