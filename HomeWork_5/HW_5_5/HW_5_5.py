with open('new_file_number.txt', 'w', encoding='utf-8') as numbers:
    user_numbers = input('Enter few numbers - ')
    numbers.write(user_numbers)
with open('new_file_number.txt', 'r', encoding='utf-8') as numbers:
  a = numbers.readline().split()
  # readline() приянть данные как строку через запятую! Не мог сразу понять как это сделать
  print(sum(map(int, a)))
