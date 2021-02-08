def f():
  stop = True
  numbers = []
  sum = 0
  while stop == True:
      user_number = input('PLease enter number or press Q to escape - ').lower().split()
      numbers.append(user_number)
      for el in range(len(user_number)):
          if user_number[el] == 'q':
              stop = False
              break
          else:
              sum = sum + int(user_number[el])
              print(sum)
user = f()
#
# def try_1():
#     user = []
#     a = 0
#     while a < 3:
#         b = input('Enter - ')
#         user.append(b)
#         a += 1
#         if a == 3:
#             print('STOP')
#             print(user)
#             break
# c = try_1()



# a = ('2, w, 7, 3, 4')
# b = a.split()
# print(b)
# c = range(len(b))
# ex = None
# print(c)
# while ex != 'q':
#
# print(c)

