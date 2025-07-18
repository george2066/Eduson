'''Модуль time в Python позволяет работать со временем.
Вам потребуется функция asctime. Она считывает
текущее время компьютера и возвращает его в удобном
виде. Напишите программу: используйте эту функцию
для отображения на экране текущей даты и времени'''

from time import asctime

def times():
    return asctime

'''Напишите программу, которая будет находить самое
длинное слово в файле.
В качестве результата программа должна выводить
на экран длину самого длинного слова и все слова
такой длины.
Важно: принимайте за значимые буквы любые символы,
включая цифры и знаки препинания, но не пробелы'''

def long_word(file):
    with open(file) as f:
        words = f.read().split()
        long_word = max(words)
        big_words = [long_word]
        for word in words:
            if len(word) == len(long_word):
                big_words.append(word)
    return big_words

'''Напишите программу, которая будет считывать содер-
жимое файла, добавлять к считанным строкам поряд-
ковый номер и сохранять их в таком виде в новом файле.
Имя исходного файла и имя целевого файла необходимо
запросить у пользователя.
Каждая строка в созданном файле должна начинаться
с ее номера, двоеточия и пробела, после чего должен
идти текст строки из исходного файла.

Важно: чтобы разбить содержимое файла на строки,
используйте функцию readlines('''

def add_line_numbers(file_name, new_file_name):
    with open(file_name, "r") as file:
        content = file.readlines()

        with open(new_file_name, "w") as new_file:
            for index, line in enumerate(content):
                new_file.write(f"{index + 1}: {line}")


'''
Напишите программу: выведите на экран объединенное
содержимое нескольких файлов, имена которых
передаются ей в качестве аргументов. При этом файлы
должны объединяться в том порядке, в котором указаны
в аргументах.
В процессе работы программа должна выдавать сооб-
щения о том, какие файлы открыть не удается, и пере-
ходить к следующим файлам.
Если программа была запущена без аргументов,
на экран должно быть выведено сообщение об ошибке.

Важно: для того, чтобы код корректно обрабатывал
ошибку, используйте конструкцию try-except
'''

def combine_files(*file_names):
    if len(file_names) == 0:
        print("Ошибка: файлы на указаны.")
        return
    else:
        combined_content = ""
        for file_name in file_names:
            try:
                with open(file_name, "r") as file:
                    combined_content += file.read() + "\n"
            except:
                print(f"Файл {file_name} не открывается.")
        print(combined_content)
        return
    
'''В языке Python для создания комментариев в коде ис-
пользуется символ #. Комментарий начинается с этого
символа и продолжается до конца строки.
Напишите программу, которая будет удалять все ком-
ментарии из исходного файла с кодом на языке Python.

Важно: пусть программа просматривает каждую строку
с помощью функции readlines(). Программа должна
удалить все содержимое, после символа # и до конца
строки с помощью функции split().

Для того, чтобы код корректно обрабатывал ошибку,
используйте конструкцию try-except.

Сохраните новое содержимое в созданном файле.
Имена файла источника и файла назначения должны
быть запрошены у пользователя. Удостоверьтесь,
что программа корректно обрабатывает ошибки
при работе с обоими файлами'''

def remove_comments(file_name, new_file_name):
    try:
        with open(file_name, "r") as file:
            content = file.readlines()
            stripped_content = []
            for line in content:
                stripped_line = line.split("#")[0].strip()
                stripped_content.append(stripped_line)
        with open(new_file_name, "w") as new_file:
            new_file.write("\n".join(stripped_content))
    except:
        print('Не удалось открыть входной файл')