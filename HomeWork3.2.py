def user_data(name=0, surname=0, year_born=0, city_of_living=0, email=0, telephone_number=0):
    name = input('Enter your name (do not use numbers) - ') # как встроить проверку на числа?
    surname = input('Enter your surname (do not use numbers) - ')
    year_born = input('Enter year of ur born - ')
    city_of_living = input('Enter the name of city where you live - ')
    email = input('Enter your email - ')
    telephone_number = input('Enter your telephone number - ')
    print(f'Name: {name},  Surname: {surname}, User Year of born: {year_born}, City: {city_of_living}, E-mail: {email},\
 Telephone: {telephone_number}')

User = user_data()

