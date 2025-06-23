'''
Напишите функцию process_args, которая принимает на вход произвольное количество позиционных и именованных аргументов и возвращает их в виде словаря.
'''
def process_args(*args, **kwargs):
    return {**{k: v for k, v in enumerate(args)}, **kwargs}


'''Напишите функцию multiply_string, которая принимает на вход строку text и целое число multiplier. Функция должна возвращать новую строку, состоящую из повторений строки text multiplier раз.

Если значение multiplier не передано, установите его по умолчанию равным 1.'''

def multiply_string(text, multiplier=1):
    return text * multiplier

'''Напишите функцию sum_of_squares, которая принимает на вход список чисел nums и использует функцию reduce и лямбда-функцию для вычисления суммы квадратов всех чисел из списка.'''

def sum_of_squares(nums):
    from functools import reduce
    return reduce(lambda summa, num: summa + num**2, nums, 0)

'''Создайте функцию divide_numbers, которая будет делить одно число на другое. Используйте блок try-except для обработки различных исключений, которые могут возникнуть при делении
 чисел. Определите, какие исключения существуют при делении чисел и учтите их при выполнении задания. В результате верните текст ошибки как строку.
 
 Добавьте к предыдущему решению блоки else и finally.'''

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError as err:
        return str(err)
    except TypeError as err:
        return str(err)
    except Exception as err:
        return str(err)
    else:
        return result
    finally:
        print("Обработка завершена.")

'''

    Создайте функцию validate_and_format_phones(phones), которая принимает на вход список phones с номерами телефонов.
    Внутри функции пройдитесь по каждому номеру в списке phones. Проверьте, что номер соответствует следующим требованиям:
    Длина номера - 11 цифр.
    Допускается указывать "+" в начале номера.
    Допустимы разделители: ' ', '-', '(' и ')' в любом месте и количестве, кроме начала. Другие разделители не допускаются.

    Первая цифра в номере должна быть '7' или '8', другие не допускаются.

    Если номер соответствует требованиям, добавьте его в результирующий список в формате +7(123)456-7890.

    Если номер не соответствует требованиям, добавьте в результирующий список строку Invalid.

    Верните результирующий список.
'''

import re

def validate_and_format_phones(phones):
    result = []
    phones = [str(phone) for phone in phones]
    replace = lambda phone: phone.replace('8', '', 1) if phone.startswith('8') else phone.replace('7', '', 1)
    regex = lambda phone: re.findall(r'(\d{3})(\d{3})(\d{2})(\d{2})', phone)

    for phone in phones:
        phone = phone.replace(' ', '').replace('+', '')
        if phone.isdigit() and len(phone) == 11:
            phone = replace(phone)
            phone = list(regex(phone)[0])
            result.append(f'+7 ({phone[0]}) {phone[1]}-{phone[2]}-{phone[3]}')

    return result


'''

    Создайте функцию find_dates_in_text(text), которая принимает на вход текст text.
    Используя регулярное выражение r, выполните поиск дат в тексте text.
    Регулярное выражение r должно соответствовать датам в формате YYYY-MM-DD, где YYYY - год, MM - месяц и DD - день.
    Верните список всех найденных дат в тексте.

    У меня проблема
    Решу с помощью регулярок!
    Теперь две проблемы
'''

def find_dates_in_text(text):
    dates = list(re.findall(r'\b\d{1,4}\-(?:[1-9]|1[0-2])\-(?:[1-9]|[12][0-9]|3[0-1])\b', text))
    return dates


'''
    Создайте функцию extract_url_without_scheme(web_url), которая принимает на вход строку web_url с URL-адресом.
    Используя регулярное выражение r, выполните поиск схемы доступа в URL-адресе.
    Удалите схему доступа из URL-адреса с помощью регулярного выражения trim.
    Верните URL-адрес без указания схемы доступа.
'''

def extract_url_without_scheme(web_url):
    web_url = re.sub(r'^(?:http|https|ftp)://', '', web_url)
    return web_url

print(extract_url_without_scheme('https://www.google.com/'))

'''Можно бы было применить ^.+//'''








