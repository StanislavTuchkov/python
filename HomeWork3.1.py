def devide_func():
    a = int(input('Enter first number - '))
    b = int(input('Enter second number - '))
    if b == 0:
        b = int(input('What? Are u seriously want to divide by 0? Dude, choose different number! - '))
    c = round((a / b), 2)
    return  c
    print(c)

ask = devide_func()
print(ask)