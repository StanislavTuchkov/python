def reg():
    words = input('Enter your word - ').lower().title()
    return words
def big_list():
    a = []
    b = 0
    while b < 3:
        c = reg()
        a.append(c)
        b +=1
    if b == 3:
        print(' '.join(a))

name = big_list()