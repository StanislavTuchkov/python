from random import randrange
ran1 = randrange(4, 15)
list = []
i = 0
random = ran1
while i < random:
    ran2 = randrange(0, 500)
    list.append(ran2)
    i += 1
    if i == random:
        break
