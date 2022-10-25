# 23.4 Вызов исключений: оператор raise

count = 0
user_file = open('people.txt', 'r', encoding='utf-8')

try:
    for line in user_file:
        len_line = len(line)
        if line.endswith('\n'):
            len_line -= 1
        if len_line < 3:
            raise ValueError
        count += len_line
    print('Сумма =:', count)
except ValueError:
    print('Файл содержит имя c количеством символов меньше 3х')
finally:
    print('Программа завершена')