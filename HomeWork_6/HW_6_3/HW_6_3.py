class Worker:
    name = 0
    surname = 0
    position = 0
    _income = {'wage': 0, 'bonus': 0}
    _income['wage'] = int(input('Enter workers wage - '))
    _income['bonus'] = int(input('Enter workers bonus - '))
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        # self.income = income

class Position(Worker):
    # def __init__(self, name, surname, position):
    #     super().__init__(name, surname, position)
    def get_full_name(self):
        return f'{self.name} {self.surname}'
    def income(self):
        return f'{sum(self._income.values())}'
    # def total(self):
    #     print(f'{income}')



name = input('Enter workers name - ')
surname = input('Enter workers surname - ')
position = input('Enter workers position - ')
a = Position(name, surname, position)
print(a.get_full_name())
print(a.income())
