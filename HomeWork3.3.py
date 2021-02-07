def sum_of_a_big():
    a = int(input('Enter first number - '))
    b = int(input('Enter second number - '))
    c = int(input('Enter third number - '))
    if a >= b and b <= c:
        sum = a + c
    elif a >= b and b >= c:
        sum = a + b
    elif a <= b and a <= c:
        sum = b + c
    print(sum)

user_numbers = sum_of_a_big()


