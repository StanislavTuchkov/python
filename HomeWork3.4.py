def exponentiation():
    x = int(input('Enter a positive number - '))
    while x < 0:
        x = int(input('Enter a positive number - '))
    y = int(input('Enter a negative integer - '))
    while y > 0:
        y = int(input('Enter a negative integer - '))
    i = x
    count = 0
    result = 1 / (i * x)
    while count < (y * -1):
        i = i * x
        count += 1
        if  count == (y * -1):
            break
    print(result)
calculating = exponentiation()

