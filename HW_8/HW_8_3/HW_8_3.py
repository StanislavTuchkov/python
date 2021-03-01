class IntCheck:
    def __init__(self, *args):
        # global user_num
        user_list = []
        while True:
            try:
                user_num = []
                num = int(input('Enter a number - '))
                user_num.append(num)
                # map(int,''.join(user_num).replace(',', '').replace(' ', ''))
                user_list.append(num)

            except ValueError:
                print(f'ERROR. Enter a number')
                stop = input('If you want to continue enter Y, if quit press Q - ').upper()
                if stop == 'Y':
                    print('Continue....')
                elif stop == 'Q':
                    print ('Program stopped!')
                    print(f'User numbers {"".join(str(user_list).replace(","," "))}')
                    return

            else:
                # print(f'Every number is {user_list}')
                print(f'User numbers {"".join(str(user_list).replace(","," "))}')
# user_num = []
# num = input('Enter a number - ')
# user_num.append(num)
# map(int,''.join(user_num).replace(',', '').replace(' ', ''))
# print(''.join(user_num).replace(',',' '))
a = IntCheck()
