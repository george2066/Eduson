'''
Напишите функцию check_list, которая принимает на вход переменную var и проверяет, является ли она списком.
'''

def check_list(var):
    return isinstance(var, list)

'''Напишите функцию get_value_by_index, которая принимает на вход список ref_list и индекс index. Функция должна вернуть значение списка ref_list по указанному индексу, если список ref_list не равен None, является списком (а не другим типом данных) и индекс не выходит за пределы длины списка. В любом ином случае верните значение None. '''

def get_value_by_index(ref_list, index):
    proff = lambda lst, index: ref_list is not None and type(ref_list) is list and len(ref_list) > index
    return ref_list[index] if proff(ref_list, index) else None

'''Напишите функцию list_reorder, которая принимает на вход список списков list_of_lists. Функция должна изменить структуру списка, так чтобы элементы из вложенных списков стали элементами одного общего списка.'''

def list_reorder(list_of_lists):
    return [el for sub in list_of_lists for el in sub]

'''Напишите функцию list_insert, которая принимает на вход список ref_list, индекс start, число num, и количество повторений rep. Функция должна вставить число num в список ref_list начиная с позиции start, повторяя его rep раз.'''

def list_insert(ref_list, start, num, rep):
    if len(ref_list) < start:
        return -1

    ref_list[start:start] = [num,] * rep

    return ref_list

'''Напишите функцию generate_values, которая принимает на вход начальное значение start и конечное значение end. Функция должна вернуть список значений в заданном числовом интервале от start до end (включительно).'''

def generate_values(start, end):
    fwd = 1 if start <= end else -1
    return list(range(start, end + 1 * fwd, 1 * fwd))

'''Даны два словаря dict1 и dict2. Напишите функцию merge_dicts, которая объединит эти два словаря в один с помощью оператора объединения и вернет результат.'''
def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

'''Даны два словаря dict1 и dict2. Напишите функцию merge_dicts, которая объединит эти два словаря. В начале результирующего словаря должны идти ключи dict1. Значения с общими ключами должны стать элементами общего списка в результирующем словаре. Функция merge_dicts должна вернуть результирующий словарь.'''

def merge_dicts(dict1, dict2):
    for key, value in dict2.items():
        if dict1.get(key):
            dict1[key] = [dict1[key], value]
        else:
            dict1[key] = value
    return dict1

"""Напишите функцию count_elements, которая принимает на вход коллекцию (список, кортеж, множество или строку) и возвращает словарь. В нем ключами должны быть уникальные элементы коллекции, а значениями - количество их вхождений в данную коллекцию. В результате верните получивышийся словарь."""

def count_elements(collection):
    result_dict = {}
    for element in collection:
        if element in result_dict:
            result_dict[element] += 1
        else:
            result_dict[element] = 1
    return result_dict

'''Напишите функцию get_value, которая принимает на вход словарь data и ключ key. Функция должна возвращать значение из словаря data, соответствующее переданному ключу key. Если ключ отсутствует в словаре, функция должна возвращать строку "Key not found".'''

def get_value(data, key):
    value = data.get(key)
    return value if value is not None else "Key not found"

'''Напишите функцию sort_dict, которая принимает на вход словарь d, тип сортировки type (keywise или valuewise) и порядок сортировки order (asc или desc). Функция должна возвращать отсортированный словарь по ключам или значениям, в зависимости от переданных параметров.'''

def sort_dict(d, type, order):
    if type == "keywise":
        idx = 0
    else:
        idx = 1

    if order == "desc":
        reverse_check = True
    else:
        reverse_check = False

    return dict(sorted(d.items(), key=lambda x: x[idx], reverse=reverse_check))













