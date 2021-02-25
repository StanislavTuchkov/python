with open('timetable.txt', 'r', encoding='utf-8') as f:
    for line in f:
        course, lessons = line.split(':')
        # print(course)
        # print(lessons)
        sum = []
        for i in lessons:
            if i == ' ' or (i >= '0' and i <= '9'):
                sum.append(i)
        print(sum)

     # print("".join([i for i in lessons if i == ' ' or (i >= '0' and i <= '9')]).split())