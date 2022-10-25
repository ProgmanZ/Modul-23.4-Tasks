# Задача 2. Логирование
# количество слов, из которых можно получить палиндром
# Если в строке встречается число, то программа выдаёт ошибку ValueError

count = 0
count_string = 0

log_file = open('errors.log', 'a+', encoding='utf-8')

user_string = str()

try:
    with open('words.txt', 'r', encoding='utf-8') as input_file:
        log_file.write('Файл words.txt найден и открыт в режиме "только чтение".\n')

        for line in input_file:
            count_string += 1
            user_string = line.strip()
            log_file.write('Чтение строки из файла words.txt\n')
            log_file.write(f'Строка содержит: "{user_string}"\n')
            if user_string.isalpha():
                if user_string == user_string[::-1]:
                    print('Палиндром найден..')
                    log_file.write(f'Строка {count_string} файла содержит палиндром: {user_string}\n')
                    count += 1
                else:
                    log_file.write(f'строка {count_string} не содержит палиндром.\n')
            else:
                log_file.close()
                raise ValueError


except ValueError:
    with open('errors.log', 'a+', encoding='utf-8') as log_file:
        log_file.write(f'!!!!!Ошибка в строке {count_string} файла\n')
        log_file.write(f'!!!!!Строка содержит данные: "{user_string}"\n')
        print('Ошибка!')
except FileNotFoundError('Ошибка! Файл words.txt не найден'):
    with open('errors.log', 'a+', encoding='utf-8') as log_file:
        log_file.write('!!!!Ошибка! Файл words.txt не найден\n')

else:
    with open('errors.log', 'a+', encoding='utf-8') as log_file:
        log_file.write(f'Выведено сообщение о найденных палиндромах в количестве: {count} слов.\n')
        log_file.write(f'Программа прочитала {count_string} строк.\n')
        log_file.write('Программа успешно завершена.\n')

finally:
    log_file.close()



