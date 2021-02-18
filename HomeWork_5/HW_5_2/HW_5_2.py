f = open('text_2.txt')
lines = 0
with open('text_2.txt') as f:
    for line in f:
        lines = lines + 1
print(f'There are {lines} lines'.upper())

f_words = open('text_2.txt')
count_words = f_words.readline()
with open('text_2.txt') as count_words:
    for index, value in enumerate(count_words):
        # number = len(value.split())
        print(f'{value.rstrip()} - {len(value.split())} words')


# with open('text_2.txt', 'r', encoding='utf-8') as f:
#     usefulness = [f'{line}. {" ".join(count.split())} - {len(count.split())} слов ' for line, count in enumerate(f, 1)]
#     print(*usefulness, f'всего строк - {len(usefulness)}.', sep='\n')

