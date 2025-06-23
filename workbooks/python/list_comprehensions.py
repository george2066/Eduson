'''Напишите функцию flatten_tuple, которая принимает на вход кортеж tup, содержащий внутри себя другие кортежи (подсписки). Функция должна вернуть список, состоящий из всех элементов подсписков.'''
def flatten_tuple(tup):
    return [el for sub in tup for el in sub]

'''Напишите функцию sum_positive_numbers, которая принимает список целых чисел numbers и возвращает сумму только положительных чисел из данного списка.'''

def sum_positive_numbers(numbers):
    return sum([el for el in numbers if el >= 0])

'''Напишите функцию process_array, которая принимает список целых чисел numbers и возвращает новый список, содержащий только положительные числа, умноженные на 2.'''
def process_array(numbers):
    return [num * 2 for num in numbers if num > 0]

'''Напишите функцию list_to_dict, которая принимает список ключей и список значений. А затем возвращает словарь, сформированный из этих списков. Используйте генератор списка и специальную функцию.'''

def list_to_dict(keys, values):
    return {key: value for key, value in zip(keys, values)}

'''Напишите функцию sum_n_dimensional_vectors, которая принимает список векторов в n-мерном пространстве и возвращает их сумму. Векторы представлены списками чисел одинаковой длины. Сумма векторов вычисляется покомпонентно.'''
def sum_n_dimensional_vectors(vectors):
    result = [0] * len(vectors[0])
    for vector in vectors:
        result = map(sum, zip(result, vector))

    return tuple(result)

'''

    Создайте функцию lim_max(nums, limit), которая принимает на вход кортеж чисел nums и ограничение limit.
    Инициализируйте переменную max_value со значением -1, которая будет хранить максимальное значение, строго меньшее limit.
    Пройдитесь циклом по элементам кортежа nums.
    Внутри цикла проверьте каждый элемент кортежа на условие: элемент должен быть строго меньше limit и больше текущего значения max_value.
    Если условие выполняется, обновите значение max_value на текущий элемент.
    По окончанию цикла, верните значение max_value.
'''
def lim_max(nums, limit):
    max_value = -1
    for el in nums:
        if el > max_value and el < limit:
            max_value = el
    return max_value

'''

    Создайте функцию lim_max(nums, limit), которая принимает на вход кортеж чисел nums и ограничение limit.
    Инициализируйте переменную max_value со значением -1, которая будет хранить максимальное значение, строго меньшее limit.
    Пройдитесь циклом по элементам кортежа nums.
    Внутри цикла проверьте каждый элемент кортежа на условие: элемент должен быть строго меньше limit и больше текущего значения max_value.
    Если условие выполняется, обновите значение max_value на текущий элемент.
    По окончанию цикла, верните значение max_value.
'''

def lim_max(nums, limit):
    max_value = max([num for num in nums if num < limit], default=-1)
    return max_value





