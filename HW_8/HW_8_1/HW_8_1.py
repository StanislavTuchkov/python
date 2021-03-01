import time
from datetime import datetime, date
class Date:

    def __init__(self, date):
        # # self.date = f'{input("Enter day - ")}-{input("Enter month - ")}-{input("Enter year - ")}'
        self.date = str(date)
        # self.date = {
        #     'Day' : int(input("Enter day - ")),
        #     'Month' : int(input("Enter month - ")),
        #     'Year' : int(input("Enter year - "))
        # }
        # a = f'{self.date["Day"] :02}-{self.date["Month"] :02}-{self.date["Year"] :02}'

    @classmethod
    def date_to_numbers(cls, date):
        for i in date:
            if i =='-':
                date_in_num = date.replace(i, ' ').split(' ')
                return int(date_in_num[0]), int(date_in_num[1]), int(date_in_num[2])

    @staticmethod
    def validate_date(date_valid):
        try:
            date = time.strptime(date_valid, '%d-%m-%Y')
            print('Date is OK')
        except:
            print('Date wrong!!!')
#
#     def __str__(self):
#         a = date(list(Date.date_to_numbers(self.date)))
#         return f'{a.strftime("%A, %d. %B %Y")}'
# #
# #
# a = Date('2-3-2012')
# b = Date.date_to_numbers('2-3-2012')
# print(a)
# print(Date.validate_date('2-3-2012'))


# aa = date()
# print(type(aa))
# print(aa.strftime("%A, %d. %B %Y"))
# a = '02 03/ 2012'
# try:
#     b = time.strptime(a, '%d %m %Y')
# except:
#     print('NOT OK')

# a = '1-2-3333'
# def num(a):
#     for i in a:
#         if i == '-':
#             num = a.replace(i, ' ').split(' ')
#             print(num[2])
#
# a = num('1-2-3333')
